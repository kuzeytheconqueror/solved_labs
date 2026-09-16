<div align="center">

# Solved Machines

**Cybersecurity Writeups & Notes — one lab at a time**

A structured collection of notes and walkthroughs for every machine and lab I solve,
from beginner warmups to more challenging boxes. Even the basic ones get a written
explanation — and for the especially instructive ones, I record a **full video solve**.

[![Obsidian Vault](https://img.shields.io/badge/vault-Obsidian-7C3AED?logo=obsidian&logoColor=white)](https://obsidian.md)
[![Hack The Box](https://img.shields.io/badge/Hack_The_Box-9FEF00?logo=hackthebox&logoColor=black)](https://www.hackthebox.com)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-212C42?logo=tryhackme&logoColor=white)](https://tryhackme.com)
[![PortSwigger](https://img.shields.io/badge/PortSwigger-FF6633?logo=portswigger&logoColor=white)](https://portswigger.net/web-security)

</div>

---

## Repository Structure

```
obsidian_notes/
├── Hackvisor/       # Hackvisor warmup machines
├── HTB/             # Hack The Box machines (coming soon)
├── Try_Hack_Me/     # TryHackMe rooms (coming soon)
├── Independent/     # Independent / miscellaneous labs
└── Burb_Suit/       # PortSwigger Web Security Academy (LLM, AI scanners, XSS, OS cmd injection, SSRF)
```

Quick index: [Solved_Machines.md](obsidian_notes/Solved_Machines.md)

---

## Solved Machines

### Hackvisor

| Machine | Focus | Writeup | Video |
|---|---|---|---|
| 007 | RDP misconfiguration, passwordless access | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Hackvisor/warmups/007.md) | — |
| Arrow | Telnet, weak credentials | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Hackvisor/warmups/Arrow.md) | — |
| Carnival | SMB enumeration & exploitation | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Hackvisor/warmups/Carnival.md) | — |
| File Hunter | FTP, anonymous access | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Hackvisor/warmups/File%20Hunter.md) | — |
| Mount | NFS misconfiguration | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Hackvisor/warmups/Mount.md) | — |
| Query Gate | MySQL, passwordless root login | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Hackvisor/warmups/Query%20Gate.md) | — |
| Reddict | Redis / NoSQL security | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Hackvisor/warmups/Reddict.md) | — |
| Secure Command | SSH basics & secure access | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Hackvisor/warmups/Secure%20Command.md) | — |
| Tiger | VNC misconfiguration | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Hackvisor/warmups/Tiger.md) | — |

### [![Hack The Box](https://img.shields.io/badge/Hack_The_Box-9FEF00?logo=hackthebox&logoColor=black)](https://www.hackthebox.com)

_No machines solved yet — coming soon._

### [![TryHackMe](https://img.shields.io/badge/TryHackMe-212C42?logo=tryhackme&logoColor=white)](https://tryhackme.com)

_No rooms solved yet — coming soon._

### [![PortSwigger](https://img.shields.io/badge/Burp_Suite_%2F_PortSwigger-FF6633?logo=portswigger&logoColor=white)](https://portswigger.net/web-security)

#### LLM Pentesting · [hub](obsidian_notes/Burb_Suit/LLM_Pentesting/LLM%20Pentesting.md)

| Lab | Difficulty | Focus | Writeup | Video |
|---|---|---|---|---|
| Exploiting LLM APIs with excessive agency | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | Excessive agency, SQL via Debug SQL API | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/LLM_Pentesting/Labs/Exploiting%20LLM%20APIs%20with%20excessive%20agency.md) | [![watch](https://img.shields.io/badge/video-watch-FF0000?logo=youtube&logoColor=white)](https://youtu.be/UG_4smygJes?si=hiMKcpKleDvfRxbT) |
| Exploiting vulnerabilities in LLM APIs | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | OS command injection via Newsletter API | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/LLM_Pentesting/Labs/Exploiting%20vulnerabilities%20in%20LLM%20APIs.md) | — |
| Indirect prompt injection | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | Indirect prompt injection via product reviews | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/LLM_Pentesting/Labs/Indirect%20prompt%20injection.md) | [![watch](https://img.shields.io/badge/video-watch-FF0000?logo=youtube&logoColor=white)](https://youtu.be/9yKL6Ni6FkY) |
| Exploiting insecure output handling in LLMs | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | Insecure output handling → XSS | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/LLM_Pentesting/Labs/Exploiting%20insecure%20output%20handling%20in%20LLMs.md) | — |

#### AI-Powered Scanner Vulnerabilities · [hub](obsidian_notes/Burb_Suit/AI-powered%20scanner%20vulnerabilities/AI-Powered%20scanner%20vulnerabilities.md)

| Lab | Difficulty | Focus | Writeup |
|---|---|---|---|
| Exploiting AI agents to perform destructive actions | ![Expert](https://img.shields.io/badge/Expert-b91c1c) | Trick the scanner into deleting `carlos` | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/AI-powered%20scanner%20vulnerabilities/labs/Exploiting%20AI%20agents%20to%20perform%20destructive%20actions.md) |
| Exploiting AI agents to exfiltrate sensitive information | ![Expert](https://img.shields.io/badge/Expert-b91c1c) | Persona injection leaks `carlos`'s API key | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/AI-powered%20scanner%20vulnerabilities/labs/Exploiting%20AI%20agents%20to%20exfiltrate%20sensitive%20information.md) |

#### Cross-Site Scripting (XSS) · [hub](obsidian_notes/Burb_Suit/XSS/XSS.md)

| Lab | Difficulty | Focus | Writeup |
|---|---|---|---|
| Reflected XSS into HTML context with nothing encoded | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | Reflected XSS in the search box | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/XSS/labs/Reflected%20XSS%20into%20HTML%20context%20with%20nothing%20encoded.md) |
| Stored XSS into HTML context with nothing encoded | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | Stored XSS in a blog comment | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/XSS/labs/Stored%20XSS%20into%20HTML%20context%20with%20nothing%20encoded.md) |
| DOM XSS in document.write sink using source location.search | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | Break out of an `img src` attribute | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/XSS/labs/DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search.md) |
| DOM XSS in document.write sink inside a select element | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | Break out of a `select` element | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/XSS/labs/DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search%20inside%20a%20select%20element.md) |
| DOM XSS in innerHTML sink using source location.search | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | `onerror` handler in the `innerHTML` sink | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/XSS/labs/DOM%20XSS%20in%20innerHTML%20sink%20using%20source%20location.search.md) |
| DOM XSS in jQuery anchor href attribute sink using location.search source | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | `javascript:` URL in a jQuery `href` sink | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/XSS/labs/DOM%20XSS%20in%20jQuery%20anchor%20href%20attribute%20sink%20using%20location.search%20source.md) |

#### OS Command Injection · [hub](obsidian_notes/Burb_Suit/OS_command_injection/OS_command_injection.md)

| Lab | Difficulty | Focus | Writeup |
|---|---|---|---|
| OS command injection, simple case | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | OS command injection in stock checker | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/OS_command_injection/labs/OS%20command%20injection,%20simple%20case.md) |
| Blind OS command injection with time delays | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | Blind, time-based | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/OS_command_injection/labs/Blind%20OS%20command%20injection%20with%20time%20delays.md) |
| Blind OS command injection with output redirection | ![Practitioner](https://img.shields.io/badge/Practitioner-d97706) | Blind, output redirection via writable folder | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/OS_command_injection/labs/Blind%20OS%20command%20injection%20with%20output%20redirection.md) |

#### Server-Side Request Forgery (SSRF) · [hub](obsidian_notes/Burb_Suit/SSRF/SSRF.md)

| Lab | Difficulty | Focus | Writeup |
|---|---|---|---|
| Basic SSRF against the local server | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | Reach `http://localhost/admin` through the stock checker | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/SSRF/labs/Basic%20SSRF%20against%20the%20local%20server.md) |

---

## Video Walkthroughs

Whenever a machine or lab turns out to be particularly interesting or instructive, I publish
a video solving it start-to-finish and link it in the tables above (look for the red
![watch](https://img.shields.io/badge/video-watch-FF0000?logo=youtube&logoColor=white) badge).

## Medium Blogs

Longer-form writeups published on [Medium](https://medium.com/@samliumay965):

- [Lab Solved: Indirect Prompt Injection (PortSwigger)](https://medium.com/@samliumay965/lab-solved-indirect-prompt-injection-portswigger-0deebc1a777a)
- [Lab Solved: Exploiting LLM APIs with Excessive Agency](https://medium.com/@samliumay965/lab-solved-exploiting-llm-apis-with-excessive-agency-cfda4611e18a)

## How to Read the Notes

All notes live in the `obsidian_notes/` [Obsidian](https://obsidian.md) vault.
Open the folder in Obsidian for the best reading experience, or just browse the
markdown files directly here on GitHub.
