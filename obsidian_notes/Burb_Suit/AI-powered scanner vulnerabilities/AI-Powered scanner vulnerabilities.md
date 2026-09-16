# AI-Powered Scanner Vulnerabilities
> **Category:** Web LLM Attacks · **Source:** [![PortSwigger](https://img.shields.io/badge/PortSwigger-Web_Security_Academy-FF6633?logo=portswigger&logoColor=white)](https://portswigger.net/web-security/llm-attacks/ai-powered-scanner-vulnerabilities)

Notes and solved labs on attacking AI-powered web application security scanners — how they work, why LLM-driven reasoning creates a new attack surface, and how indirect prompt injection turns a scanner into an attacker's proxy.

## Notes

1. [[01_AI-powered scanner vulnerabilities]] — What AI-powered scanners are, and how they differ from traditional DAST scanners.
2. [[02_AI-powered scanner vulnerabilities]] — Indirect prompt injection in scanners, crafting effective prompts, and data exfiltration.

## Labs

| Lab | Difficulty | Key Technique |
|---|---|---|
| [[Exploiting AI agents to perform destructive actions]] | ![Expert](https://img.shields.io/badge/Expert-b91c1c) | Stored XSS / IDOR in a comment tricks the scanner into deleting `carlos` |
| [[Exploiting AI agents to exfiltrate sensitive information]] | ![Expert](https://img.shields.io/badge/Expert-b91c1c) | Persona-framed injection makes the scanner post `carlos`'s API key |

### Up next

| Lab | Key Technique |
|---|---|
| [Exploiting AI agents to trigger secondary vulnerabilities](https://portswigger.net/web-security/llm-attacks/ai-powered-scanner-vulnerabilities/lab-exploiting-target-website-vulnerabilities-to-bypass-restrictions) | Chain prompt injection with Host-header routing-based SSRF |

## References

- See [[Burb_Suit/AI-powered scanner vulnerabilities/References]].

## Status

In progress. Two labs solved; *Exploiting AI agents to trigger secondary vulnerabilities* still to do.
