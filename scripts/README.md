# Deployment checks

`python3 scripts/check_deployment.py` checks German and English routes on the
apex domain, www domain and GitHub Pages hostname. It verifies successful HTTP
responses, canonical redirects, language, form POST endpoint, expected fields
and direct email links. It uses Python's standard library only.

The Deployment smoke test workflow runs after a successful github-pages
 deployment and can also be run manually from Actions. The workflow must be
merged into the default branch before its triggers are available.

The optional manual input "Send six real Formspree enquiries" runs with
`--submit`. This uses up to six monthly submissions and sends clearly labelled
test messages. There are no submission retries; failures stop the run. Confirm
inbox delivery separately. These are HTTP checks, not browser JavaScript or
visual tests.

Initial live validation: all six page checks passed. Formspree rejected the
first submission with Cloudflare error 1010 (browser_signature_banned). No
submission was confirmed accepted; the remaining submissions were not attempted.
Resolve that restriction with Formspree before enabling live automation. The
routine read-only checks do not contact Formspree or consume submission quota.
