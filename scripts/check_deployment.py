#!/usr/bin/env python3
"""Check deployed pages; --submit sends six real Formspree test enquiries."""
import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import urllib.error
import urllib.parse
import urllib.request

BASES = ('https://walleringrobotics.de', 'https://www.walleringrobotics.de',
         'https://walleringrobotics.github.io')
ENDPOINT = 'https://formspree.io/f/mbggqaev'


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.language = None
        self.form = None
        self.fields = {}
        self.in_form = False
        self.mail_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.language = attrs.get('lang')
        if tag == 'a' and attrs.get('href') == 'mailto:ryan@walleringrobotics.de':
            self.mail_link = True
        if tag == 'form':
            self.in_form = attrs.get('id') == 'pform'
            if self.in_form:
                self.form = attrs
        if self.in_form and tag in ('input', 'textarea', 'select') and attrs.get('name'):
            self.fields[attrs['name']] = attrs.get('value', '')

    def handle_endtag(self, tag):
        if tag == 'form':
            self.in_form = False


def check(submit=False):
    stamp = datetime.now(timezone.utc).isoformat()
    pages = []
    for base in BASES:
        for path, language in (('/', 'de'), ('/en/', 'en')):
            url = base + path
            with urllib.request.urlopen(url, timeout=30) as response:
                assert response.status == 200, url
                assert response.url == BASES[0] + path, (url, response.url)
                page = Page()
                page.feed(response.read().decode('utf-8'))
            assert page.language == language, url
            assert page.form and page.form.get('action') == ENDPOINT, url
            assert page.form.get('method', '').upper() == 'POST', url
            assert page.mail_link, url
            assert {'name', 'contact', 'msg', 'sprache', '_gotcha'} <= page.fields.keys(), url
            assert page.fields['sprache'] == language.upper(), url
            pages.append((url, page))
            print('PASS page, redirect, language, form and email link:', url, flush=True)
    if submit:
        # No automatic retries: a timed-out request may already have sent mail.
        for url, page in pages:
            fields = dict(page.fields)
            fields.update(name='Deployment test for Ryan', contact='ryan@walleringrobotics.de',
                          kind='Website test', _gotcha='',
                          msg=f'TEST ONLY — requested deployment check. No customer action needed.\nSource: {url}\nRun: {stamp}')
            request = urllib.request.Request(ENDPOINT,
                data=urllib.parse.urlencode(fields).encode(),
                headers={'Accept': 'application/json', 'Referer': url})
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    result = json.load(response)
                    assert response.status == 200 and result.get('ok') is True, result
            except urllib.error.HTTPError as error:
                detail = error.read().decode('utf-8', errors='replace')[:1500]
                raise RuntimeError(f'Formspree rejected {url}: HTTP {error.code}: {detail}') from None
            print('PASS Formspree accepted test:', url, flush=True)
        print('Six submissions accepted. Inbox delivery must be confirmed separately.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--submit', action='store_true', help='Send six real test enquiries (uses quota)')
    check(parser.parse_args().submit)
