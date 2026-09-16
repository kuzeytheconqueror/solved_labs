# What is OS Command Injection?
> **Category:** OS Command Injection · **Source:** [PortSwigger Web Security Academy](https://portswigger.net/web-security/os-command-injection)

In this section, we explain what OS command injection is, and describe how these vulnerabilities can be detected and exploited. We also show some useful commands and techniques for different operating systems, and describe how to prevent OS command injection.

![[Screenshot from 2026-08-25 14-59-54.png]]

OS command injection is also known as shell injection. It allows an attacker to execute operating system (OS) commands on the server that is running an application, and typically to fully compromise the application and its data. Often, an attacker can leverage an OS command injection vulnerability to compromise other parts of the hosting infrastructure, and exploit trust relationships to pivot the attack to other systems within the organization.
