# Cross-Site Scripting (XSS)
> **Category:** Cross-Site Scripting · **Source:** [![PortSwigger](https://img.shields.io/badge/PortSwigger-Web_Security_Academy-FF6633?logo=portswigger&logoColor=white)](https://portswigger.net/web-security/cross-site-scripting)

Notes and solved labs on cross-site scripting — the three main varieties (reflected, stored, DOM-based), how to find and test for each, their impact, and defenses.

## Notes

### Fundamentals

1. [[00_Cross-site Scripting]] — Section overview.
2. [[01_What is cross-site scripting (XSS)?]] — Definition and why XSS matters.
3. [[02_How does XSS work?]] — Returning malicious JavaScript to users.
4. [[03_XSS proof of concept]] — `alert()` vs `print()` for PoCs.
5. [[04_What are the types of XSS attacks?]] — Reflected, stored, and DOM-based.
6. [[05_Reflected cross-site scripting]] — Reflected XSS in brief.
7. [[06_Stored cross-site scripting]] — Stored XSS in brief.
8. [[07_DOM-Based cross-site scripting]] — DOM XSS in brief.
9. [[08_What can XSS be used for?]] — Attacker capabilities.
10. [[09_Impact of XSS Vulnerabilities]] — Severity by application context.
11. [[10_How to find and test for XSS Vulnerabilities]] — Manual and automated testing.
12. [[11_Content Security Policy]] — CSP as a mitigation.
13. [[12_Dangling markup Injection]] — Capturing data when full XSS is blocked.
14. [[13_How to prevent XSS attacks]] — Input filtering, output encoding, headers, CSP.
15. [[14_Common Questions about cross-site scripting]] — FAQ.

### Reflected XSS

1. [[11_What is Reflected XSS]] — Definition and worked example.
2. [[12_Impact of reflected XSS attack]] — Why delivery matters.
3. [[13_Reflected XSS in different contexts]] — Context determines the payload.
4. [[14_How to find and test for reflected XSS vulnerabilities]] — Testing methodology.
5. [[15_Common questions about reflected cross-site scripting]] — FAQ.

### Stored XSS

1. [[21_Stored XSS]] — Definition and worked example.
2. [[22_Impact of stored XSS attacks]] — Self-contained delivery.
3. [[23_Stored XSS in different contexts]] — Context determines the payload.
4. [[24_How to find and test for stored XSS vulnerabilities]] — Entry and exit points.

### DOM-Based XSS

1. [[31_DOM-based XSS]] — Sources, sinks, and taint flow.
2. [[32_How to test for DOM-based cross-site scripting]] — Testing HTML and JS execution sinks.
3. [[33_Exploiting DOM XSS with different sources and sinks]] — `document.write`, `innerHTML`, and jQuery sinks.

## Labs

| Lab | Difficulty | Key Technique |
|---|---|---|
| [[Reflected XSS into HTML context with nothing encoded]] | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | `<script>alert(1)</script>` in the search box |
| [[Stored XSS into HTML context with nothing encoded]] | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | `<script>alert(1)</script>` in a comment |
| [[DOM XSS in document.write sink using source location.search]] | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | Break out of an `img src` attribute |
| [[DOM XSS in document.write sink using source location.search inside a select element]] | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | Break out of a `select` element |
| [[DOM XSS in innerHTML sink using source location.search]] | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | `<img src=1 onerror=alert(1)>` in the `innerHTML` sink |
| [[DOM XSS in jQuery anchor href attribute sink using location.search source]] | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | `javascript:` URL in a jQuery `href` sink |

## References

- [PortSwigger Web Security Academy — Cross-site scripting](https://portswigger.net/web-security/cross-site-scripting)

## Status

In progress. Stopped at: another potential sink to look out for is jQuery's `$()` selector function, which can be used to inject malicious objects into the DOM.
