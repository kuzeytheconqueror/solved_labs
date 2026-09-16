# How to Prevent OS Command Injection Attacks
> **Category:** OS Command Injection · **Source:** [PortSwigger Web Security Academy](https://portswigger.net/web-security/os-command-injection)

The most effective way to prevent OS command injection vulnerabilities is to never call out to OS commands from application-layer code. In almost all cases, there are safer ways to implement the required functionality using platform APIs.

If you have to call out to OS commands with user-supplied input, then you must perform strong input validation. Some examples of effective validation include:

- Validating against an allowlist of permitted values.
- Validating that the input is a number.
- Validating that the input contains only alphanumeric characters, with no other syntax or whitespace.

Never attempt to sanitize input by escaping shell metacharacters. In practice, this is too error-prone and vulnerable to being bypassed by a skilled attacker.

## Read more

- [Find OS command injection vulnerabilities using Burp Suite's web vulnerability scanner](https://portswigger.net/burp/vulnerability-scanner)
- [PortSwigger Research — Hunting Asynchronous Vulnerabilities (44Con and BSides Manchester)](https://portswigger.net/research/hunting-asynchronous-vulnerabilities)
