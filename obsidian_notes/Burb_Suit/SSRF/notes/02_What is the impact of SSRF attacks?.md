# What is the Impact of SSRF Attacks?
> **Category:** Server-Side Request Forgery (SSRF) · **Source:** [PortSwigger Web Security Academy](https://portswigger.net/web-security/ssrf)

A successful SSRF attack can often result in unauthorized actions or access to data within the organization. This can be in the vulnerable application, or on other back-end systems that the application can communicate with. In some situations, the SSRF vulnerability might allow an attacker to perform arbitrary command execution.

An SSRF exploit that causes connections to external third-party systems might result in malicious onward attacks. These can appear to originate from the organization hosting the vulnerable application.

| Target of the forged request | Typical outcome |
|---|---|
| The server itself (`localhost`) | Bypass access controls on admin interfaces |
| Internal back-end systems (private IPs) | Reach services that are never exposed to the internet |
| External third-party systems | Onward attacks that appear to come from the victim organization |
