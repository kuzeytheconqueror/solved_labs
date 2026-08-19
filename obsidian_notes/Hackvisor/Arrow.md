# Arrow

> **Platform:** Hackvisor · **Difficulty:** Warmup · **Topics:** Telnet, Nmap, Default Credentials

## Introduction

The Arrow warmup machine offers an easy and enjoyable starting point for
beginners in the world of cybersecurity. How can a machine be hacked using
weak authentication credentials over a telnet service? While searching for
the answer to this question, you will learn both the technical challenges of
this machine and the basic concepts in cybersecurity.

For beginners, working with this type of machine develops not only technical
skills but also problem-solving abilities. This article will assist in gaining
practical experience as well as hands-on reinforcement of theoretical
knowledge, which is critical in cybersecurity.

## What is telnet

Telnet (Teletype Network) is a text-based network protocol used to connect
to a computer remotely. Developed in 1969 and widely used in the early
days of the Internet, it is specifically designed for interacting with network
devices, servers or other endpoints. It provides a login interface with a
username and password so that users can execute commands as if they
were on the local terminal of that computer.

The major disadvantage of Telnet is that data transmission is not encrypted.
This means that any information transmitted, especially usernames and
passwords, can potentially be intercepted by malicious actors. This
vulnerability makes Telnet an especially risky option in modern network
environments where sensitive data is processed.

The following command sequence is used to connect to a server with the
telnet protocol.

```bash
telnet <SERVER-IP-ADDRESS> <PORT-NUMBER>
```

Note: If the telnet service uses port 23 by default, we do not need to specify
a port number when connecting.

**Note:** After this point, we will just be making a telnet request to the specific IP. That's all.

## Information Gathering

In cybersecurity, every successful attack is based on gathering in-depth
information about the target system. In this sense, the "Information
Gathering" process is critical to the success of attacks against the target
machine. In this section, we will cover the first and most important stage of
the penetration process, the information gathering steps involving the
Telnet service.

At this stage, we are aiming to obtain detailed information by performing
scans directly on the target system. With our scans, more specific
information is obtained, such as the version of the Telnet service, the ports it
is running on, and other service information running on the system.

The tools and methods to be used in this process may vary depending on the
structure and security level of the target system. For example, popular port
scanning tools such as `nmap` and `rustscan` can be used at this stage.

## nmap

Nmap (Network Mapper) is a powerful open-source tool widely used in
network security. Its main function is to perform network scans to detect the
existence of devices on the network, the services they run and open ports. It
is used by cybersecurity experts to find vulnerabilities, map network
structures and test security defenses.

Nmap has a command-line based interface and offers a flexible and wide
range of scanning options.

The usage and some important parameters of the Nmap tool are as follows.

```bash
nmap <TARGET>
```

- `-sS` — It scans the ports of the target machine with TCP SYN packets: `nmap -sS <TARGET>`
- `-sT` — It scans the ports of the target machine with TCP Connect packets: `nmap -sT <TARGET>`
- `-sV` — Detects the versions of services running on the target machine: `nmap -sV <TARGET>`
- `-A` — Aggressive scanning. Performs a comprehensive scan on the target, including service version, operating system detection and script scanning: `nmap -A <TARGET>`
- `-O` — It tries to detect the operating system running on the target system: `nmap -O <TARGET>`
- `-p` — Used to scan specific ports or a range of ports:
  - `nmap -p 80,443 <TARGET>` — Scans ports 80 and 443.
  - `nmap -p 1-2000 <TARGET>` — Scans ports between 1 and 2000.
  - `nmap -p- <TARGET>` — Scans all ports (65,536).

## Task 1, Task 2

We run the nmap scan at the target host.

```bash
nmap 172.20.23.22
```

And then it gives the results of the scan basically.

## Initial Access

This is the stage where the knowledge gained in the previous information
gathering phase is put into practical application and the first real interaction
with the target system begins. This is a critical step in making a
comprehensive assessment of the security status of the system.

Activities performed during the access phase usually include exploiting
vulnerabilities, bypassing firewalls and privilege escalations on the system.
During this process, ethical hackers or security analysts test the security
measures in the target system and identify potential vulnerabilities.

## Task 3, Task 4

We will try to connect to the telnet service that we discovered working by
doing a port scan in the previous step. For this, let's run the following
command.

```bash
telnet 172.20.23.22
```

When trying to connect to the target machine with Telnet, we get a hint. The
hint tells us to try very simple passwords that can be used by default, such
as `root` for the username and `root` for the password.

Also, in the line that says arrow login, we see that the hostname of the
machine we are trying to connect to is `arrow`.

## Task 5

To complete task 5, let's login with the `root:root` credentials given to us as
a hint.

**note:** Basically we use the hints to enter the system.
