WALLERING ROBOTICS — WEBSITE PACKAGE
=====================================

Contents
  index.html        the website (German, main version)
  en/index.html     English version, generated from the German page
  sitemap.xml, robots.txt  help search engines find both languages
  impressum.html    legal notice (template)
  datenschutz.html  privacy policy (template)
  legal.css         styles for the two legal pages
  favicon.svg       browser tab icon
  fonts/            self-hosted fonts (no Google connection, GDPR-safe)

Upload the CONTENTS of this folder (not the folder itself) to the web root
of your host, so that index.html sits at the top level.


BEFORE GOING LIVE — replace every [PLACEHOLDER]
-----------------------------------------------
index.html
  [E-MAIL]            contact address shown under the form
  [FORMSPREE-ID]      form endpoint ID from formspree.io (see below)
  [PILOTKONDITIONEN]  pilot terms, or delete that bullet

impressum.html
  [VORNAME NACHNAME], [STRASSE HAUSNUMMER], [PLZ] [ORT]
  [TELEFONNUMMER], [E-MAIL]
  Umsatzsteuer: keep EITHER the USt-IdNr line OR the Kleinunternehmer line
  [DEU-RP-…]  LBA operator registration number (drone section is optional;
              delete it if you don't want it shown)
  [VERSICHERER]

datenschutz.html
  Same name/address/e-mail as above
  [PRÜFEN: …] (3x)  confirm GitHub's and Formspree's legal basis for US
                    transfers and Google Workspace's contracting entity,
                    then write the confirmed text in

GitHub Pages
  CNAME       tells GitHub Pages the custom domain (walleringrobotics.de)
  .nojekyll   serves the files as-is, without Jekyll processing

The legal pages are templates, not legal advice. Have them checked
(e.g. against an e-recht24 / IT-Recht Kanzlei generator, or a lawyer).


CONTACT FORM (Formspree — works on any host, incl. GoDaddy)
-----------------------------------------------------------
1. Create a free account at formspree.io, add a new form, and set the
   notification e-mail to your inbox.
2. Copy the form ID (the part after /f/ in the endpoint URL).
3. In index.html replace [FORMSPREE-ID] with it.
Until you do, the form tells visitors to write to [E-MAIL] instead.


LANGUAGES
---------
The German page (index.html) is the source. The English page (en/index.html)
was generated from it with a translation list, so layout and code are
identical. When you change text on one page, change the other one too.
Impressum and Datenschutz exist in German only; the English page links to
them marked "(German)", which is sufficient for a German business.
