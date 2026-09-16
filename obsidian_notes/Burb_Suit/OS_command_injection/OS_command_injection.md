# OS Command Injection
> **Category:** OS Command Injection · **Source:** [![PortSwigger](https://img.shields.io/badge/PortSwigger-Web_Security_Academy-FF6633?logo=portswigger&logoColor=white)](https://portswigger.net/web-security/os-command-injection)

Notes and solved labs on OS command injection (shell injection) — how attacker input reaches a shell, in-band and blind exploitation, useful metacharacters, and defenses.

## Notes

1. [[01_What is command injection]] — What OS command injection is and why it matters.
2. [[02_Injecting OS commands]] — A worked example of chaining commands with `&`.
3. [[03_Useful commands]] — Quick reference of Linux and Windows recon commands.
4. [[04_Blind OS command injection vulnerabilities]] — Time delays, output redirection, and out-of-band (OAST) techniques.
5. [[05_Ways to inject OS commands]] — Shell metacharacters and command separators.
6. [[06_How to prevent OS command injection attacks]] — Avoiding shell calls and validating input.

## Labs

| Lab | Difficulty | Key Technique |
|---|---|---|
| [[OS command injection, simple case]] | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | `whoami` via the `storeID` stock-checker parameter |
| [[Blind OS command injection with time delays]] | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | `ping` delay confirms blind execution |
| [[Blind OS command injection with output redirection]] | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | Redirect output into the web root, then fetch it |

## Status

Finished.
