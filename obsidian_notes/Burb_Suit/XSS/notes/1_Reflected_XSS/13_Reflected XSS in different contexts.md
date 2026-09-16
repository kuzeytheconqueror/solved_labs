# Reflected XSS in Different Contexts
> **Category:** Cross-Site Scripting (XSS) · **Source:** [PortSwigger Web Security Academy](https://portswigger.net/web-security/cross-site-scripting)

There are many different varieties of reflected cross-site scripting. The location of the reflected data within the application's response determines what type of payload is required to exploit it and might also affect the impact of the vulnerability.

In addition, if the application performs any validation or other processing on the submitted data before it is reflected, this will generally affect what kind of XSS payload is needed.