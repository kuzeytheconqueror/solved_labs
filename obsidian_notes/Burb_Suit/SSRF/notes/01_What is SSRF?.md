# What is SSRF?
> **Category:** Server-Side Request Forgery (SSRF) · **Source:** [PortSwigger Web Security Academy](https://portswigger.net/web-security/ssrf)

Server-side request forgery is a web security vulnerability that allows an attacker to cause the server-side application to make requests to an unintended location.

In a typical SSRF attack, the attacker might cause the server to make a connection to internal-only services within the organization's infrastructure. In other cases, they may be able to force the server to connect to arbitrary external systems. This could leak sensitive data, such as authorization credentials.

![[Screenshot from 2026-09-11 13-58-28.png]]

> [!tip] In one sentence
> The attacker cannot reach the internal system directly, so they make the **website** reach it for them — the server becomes a proxy that sits on the trusted side of the firewall.
