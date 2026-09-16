# Lab: Blind OS Command Injection with Time Delays
> **Platform:** PortSwigger Web Security Academy · **Difficulty:** Practitioner · **Topics:** OS Command Injection, Blind

## Description

This lab contains a blind OS command injection vulnerability in the feedback function.

The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response.

To solve the lab, exploit the blind OS command injection vulnerability to cause a 10 second delay.

## Solution

1. Use Burp Suite to intercept and modify the request that submits feedback.
2. Modify the `email` parameter, changing it to:

	```text
	email=x||ping+-c+10+127.0.0.1||
	```

3. Observe that the response takes 10 seconds to return.

## Reference

- [PortSwigger — Blind OS command injection with time delays](https://portswigger.net/web-security/os-command-injection/lab-blind-time-delays)
- Related notes: [[04_Blind OS command injection vulnerabilities]]
