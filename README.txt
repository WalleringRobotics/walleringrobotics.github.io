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


WEBSITE CONFIGURATION
-----------------------------------------------
index.html
  Contact email and Formspree endpoint are configured in both language pages.
  Pilot terms are negotiated individually and are not listed on the site.

impressum.html
  Owner: Ryan Matthews, Wallering 29, 84577 Tüßling, Deutschland
  Phone: +49 176 34599887; email: ryan@walleringrobotics.de
  VAT and drone registration/insurance sections removed at the owner's request.
  No Kleinunternehmer status is asserted.

datenschutz.html
  Owner, address and email are configured as above.
  The policy describes GitHub Pages hosting, Formspree submissions and
  Google Workspace email. Unverified certification and contract claims
  have been removed; this does not establish legal completeness.

GitHub Pages
  CNAME       tells GitHub Pages the custom domain (walleringrobotics.de)
  .nojekyll   serves the files as-is, without Jekyll processing

The legal pages are templates, not legal advice. Have them checked
(e.g. against an e-recht24 / IT-Recht Kanzlei generator, or a lawyer).


CONTACT FORM (Formspree — works on any host, incl. GoDaddy)
-----------------------------------------------------------
Both language pages submit to https://formspree.io/f/mbggqaev.
In the Formspree dashboard, verify ryan@walleringrobotics.de as the
notification recipient. After deployment, test both language forms and
confirm that submissions appear in Formspree and arrive in the inbox.
If replacing the endpoint later, update index.html and en/index.html.
Direct email links remain available as an alternative.


LANGUAGES
---------
The German page (index.html) is the source. The English page (en/index.html)
was generated from it with a translation list, so layout and code are
identical. When you change text on one page, change the other one too.
Impressum and Datenschutz exist in German only; the English page links to
them marked "(German)", which is sufficient for a German business.
