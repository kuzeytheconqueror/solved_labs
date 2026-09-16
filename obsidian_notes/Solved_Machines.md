# Solved Machines & Labs

> This is my Obsidian vault to preserve all my labs that I solved with notes.
> Open this folder in [Obsidian](https://obsidian.md) for the best reading experience.

---

## Hackvisor

| Machine | Focus | Writeup |
|---|---|---|
| 007 | RDP misconfiguration, passwordless access | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Hackvisor/warmups/007.md) |
| Arrow | Telnet, weak credentials | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Hackvisor/warmups/Arrow.md) |
| Carnival | SMB enumeration & exploitation | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Hackvisor/warmups/Carnival.md) |
| File Hunter | FTP, anonymous access | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Hackvisor/warmups/File%20Hunter.md) |
| Mount | NFS misconfiguration | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Hackvisor/warmups/Mount.md) |
| Query Gate | MySQL, passwordless root login | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Hackvisor/warmups/Query%20Gate.md) |
| Reddict | Redis / NoSQL security | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Hackvisor/warmups/Reddict.md) |
| Secure Command | SSH basics & secure access | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Hackvisor/warmups/Secure%20Command.md) |
| Tiger | VNC misconfiguration | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Hackvisor/warmups/Tiger.md) |

## [![Burp Suite / PortSwigger](https://img.shields.io/badge/Burp_Suite_%2F_PortSwigger-FF6633?logo=portswigger&logoColor=white)](https://portswigger.net/web-security)

### LLM Pentesting

Topic hub: [LLM Pentesting](Burb_Suit/LLM_Pentesting/LLM%20Pentesting.md)

| Lab | Difficulty | Focus | Writeup | Video |
|---|---|---|---|---|
| Exploiting LLM APIs with excessive agency | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | LLM, excessive agency, SQL via Debug SQL API | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/LLM_Pentesting/Labs/Exploiting%20LLM%20APIs%20with%20excessive%20agency.md) | [![watch](https://img.shields.io/badge/video-watch-FF0000?logo=youtube&logoColor=white)](https://youtu.be/UG_4smygJes?si=hiMKcpKleDvfRxbT) |
| Exploiting vulnerabilities in LLM APIs | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | LLM, OS command injection via Newsletter API | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/LLM_Pentesting/Labs/Exploiting%20vulnerabilities%20in%20LLM%20APIs.md) | — |
| Indirect prompt injection | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | LLM, indirect prompt injection via product reviews | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/LLM_Pentesting/Labs/Indirect%20prompt%20injection.md) | — |
| Exploiting insecure output handling in LLMs | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | LLM, insecure output handling, XSS | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/LLM_Pentesting/Labs/Exploiting%20insecure%20output%20handling%20in%20LLMs.md) | — |

### OS Command Injection

Topic hub: [OS Command Injection](Burb_Suit/OS_command_injection/OS_command_injection.md)

| Lab | Difficulty | Focus | Writeup |
|---|---|---|---|
| OS command injection, simple case | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | OS command injection in stock checker | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/OS_command_injection/labs/OS%20command%20injection,%20simple%20case.md) |
| Blind OS command injection with time delays | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | Blind OS command injection, time-based | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/OS_command_injection/labs/Blind%20OS%20command%20injection%20with%20time%20delays.md) |
| Blind OS command injection with output redirection | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | Blind OS command injection, output redirection via writable folder | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/OS_command_injection/labs/Blind%20OS%20command%20injection%20with%20output%20redirection.md) |

### Cross-Site Scripting (XSS)

Topic hub: [Cross-Site Scripting (XSS)](Burb_Suit/XSS/XSS.md)

| Lab | Difficulty | Focus | Writeup |
|---|---|---|---|
| Reflected XSS into HTML context with nothing encoded | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | Reflected XSS in the search box | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/XSS/labs/Reflected%20XSS%20into%20HTML%20context%20with%20nothing%20encoded.md) |
| Stored XSS into HTML context with nothing encoded | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | Stored XSS in a blog comment | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/XSS/labs/Stored%20XSS%20into%20HTML%20context%20with%20nothing%20encoded.md) |
| DOM XSS in document.write sink using source location.search | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | Break out of an `img src` attribute | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/XSS/labs/DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search.md) |
| DOM XSS in document.write sink inside a select element | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | Break out of a `select` element | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/XSS/labs/DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search%20inside%20a%20select%20element.md) |
| DOM XSS in innerHTML sink using source location.search | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | `onerror` handler in the `innerHTML` sink | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/XSS/labs/DOM%20XSS%20in%20innerHTML%20sink%20using%20source%20location.search.md) |
| DOM XSS in jQuery anchor href attribute sink using location.search source | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | `javascript:` URL in a jQuery `href` sink | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/XSS/labs/DOM%20XSS%20in%20jQuery%20anchor%20href%20attribute%20sink%20using%20location.search%20source.md) |

### Server-Side Request Forgery (SSRF)

Topic hub: [Server-Side Request Forgery (SSRF)](Burb_Suit/SSRF/SSRF.md)

| Lab | Difficulty | Focus | Writeup |
|---|---|---|---|
| Basic SSRF against the local server | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | Reach `http://localhost/admin` through the stock checker | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/SSRF/labs/Basic%20SSRF%20against%20the%20local%20server.md) |

### AI-Powered Scanner Vulnerabilities

Topic hub: [AI-Powered Scanner Vulnerabilities](Burb_Suit/AI-powered%20scanner%20vulnerabilities/AI-Powered%20scanner%20vulnerabilities.md)

| Lab | Difficulty | Focus | Writeup |
|---|---|---|---|
| Exploiting AI agents to perform destructive actions | ![Expert](https://img.shields.io/badge/Expert-b91c1c) | Trick the scanner into deleting `carlos` | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/AI-powered%20scanner%20vulnerabilities/labs/Exploiting%20AI%20agents%20to%20perform%20destructive%20actions.md) |
| Exploiting AI agents to exfiltrate sensitive information | ![Expert](https://img.shields.io/badge/Expert-b91c1c) | Persona injection leaks `carlos`'s API key | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](Burb_Suit/AI-powered%20scanner%20vulnerabilities/labs/Exploiting%20AI%20agents%20to%20exfiltrate%20sensitive%20information.md) |

## [![Hack The Box](https://img.shields.io/badge/Hack_The_Box-9FEF00?logo=hackthebox&logoColor=black)](https://www.hackthebox.com)

_No machines solved yet — coming soon._

## [![TryHackMe](https://img.shields.io/badge/TryHackMe-212C42?logo=tryhackme&logoColor=white)](https://tryhackme.com)

_No rooms solved yet — coming soon._
