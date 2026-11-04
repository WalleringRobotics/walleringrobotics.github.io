Visitors can now click ryan@walleringrobotics.de in the German and English contact sections to open their email application. The existing form fallback also displays the real address instead of [E-MAIL].

Validation: git diff --check passed; both pages contain the matching mailto link and displayed address. Email delivery was not tested.

Remaining Formspree setup: the contact form still points to /f/[FORMSPREE-ID], so it cannot submit yet. Create a form in Formspree, configure and verify ryan@walleringrobotics.de as the recipient, then replace [FORMSPREE-ID] in index.html and en/index.html with the supplied form ID. Test submission and inbox delivery after configuration. No account credentials or form ID were supplied, so this PR enables direct email links without claiming the form works.
