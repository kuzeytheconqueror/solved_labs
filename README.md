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
└── Burb_Suit/       # Burp Suite & PortSwigger labs (LLM pentesting, OS command injection)
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

| Lab | Focus | Writeup | Video |
|---|---|---|---|
| Exploiting LLM APIs with excessive agency | LLM, excessive agency, SQL via Debug SQL API | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/LLM_Pentesting/Labs/Exploiting%20LLM%20APIs%20with%20excessive%20agency.md) | [![watch](https://img.shields.io/badge/video-watch-FF0000?logo=youtube&logoColor=white)](https://youtu.be/UG_4smygJes?si=hiMKcpKleDvfRxbT) |
| Exploiting vulnerabilities in LLM APIs | LLM, OS command injection via Newsletter API | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/LLM_Pentesting/Labs/Exploiting%20vulnerabilities%20in%20LLM%20APIs.md) | — |
| Indirect prompt injection | LLM, indirect prompt injection via product reviews | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/LLM_Pentesting/Labs/Indirect%20prompt%20injection.md) | [![watch](https://img.shields.io/badge/video-watch-FF0000?logo=youtube&logoColor=white)](https://youtu.be/9yKL6Ni6FkY) |
| Exploiting insecure output handling in LLMs | LLM, insecure output handling, XSS | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/LLM_Pentesting/Labs/Exploiting%20insecure%20output%20handling%20in%20LLMs.md) | — |
| OS command injection, simple case | OS command injection in stock checker | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/OS_command_injection/labs/OS%20command%20injection,%20simple%20case.md) | — |
| Blind OS command injection with time delays | Blind OS command injection, time-based | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/OS_command_injection/labs/Blind%20OS%20command%20injection%20with%20time%20delays.md) | — |
| Blind OS command injection with output redirection | Blind OS command injection, output redirection via writable folder | [![notes](https://img.shields.io/badge/writeup-notes-7C3AED?logo=obsidian&logoColor=white)](obsidian_notes/Burb_Suit/OS_command_injection/labs/Blind%20OS%20command%20injection%20with%20output%20redirection.md) | — |

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
