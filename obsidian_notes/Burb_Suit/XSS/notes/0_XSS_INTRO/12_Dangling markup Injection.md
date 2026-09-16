# Dangling Markup Injection
> **Category:** Cross-Site Scripting (XSS) · **Source:** [PortSwigger Web Security Academy](https://portswigger.net/web-security/cross-site-scripting)

Dangling markup injection is a technique that can be used to capture data cross-domain in situations where a full cross-site scripting exploit is not possible, due to input filters or other defenses. It can often be exploited to capture sensitive information that is visible to other users, including CSRF tokens that can be used to perform unauthorized actions on behalf of the user.