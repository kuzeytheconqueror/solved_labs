# Lab: OS Command Injection, Simple Case
> **Platform:** PortSwigger Web Security Academy · **Difficulty:** Apprentice · **Topics:** OS Command Injection

## Description

This lab contains an OS command injection vulnerability in the product stock checker.

The application executes a shell command containing user-supplied product and store IDs, and returns the raw output from the command in its response.

To solve the lab, execute the `whoami` command to determine the name of the current user.

## Solution

1. Use Burp Suite to intercept and modify a request that checks the stock level.
2. Modify the `storeID` parameter, giving it the value `1|whoami`.
3. Observe that the response contains the name of the current user.

## Reference

- [PortSwigger — OS command injection, simple case](https://portswigger.net/web-security/os-command-injection/lab-simple)
- Related notes: [[02_Injecting OS commands]]
