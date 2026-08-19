# Carnival

> **Platform:** Hackvisor · **Difficulty:** Warmup · **Topics:** SMB, Enumeration, smbclient, Anonymous Access

## Introduction

The Carnival warmup machine is an ideal starting point for practicing with
the Server Message Block (SMB) protocol. On this machine, you will learn
how to identify vulnerabilities of the SMB service and how to work around
them. You will also learn about the basic principles of SMB and its
interactions on the network. This exercise will help you increase your
knowledge of the security of the SMB protocol.

## Server Message Block (SMB)

The SMB protocol is a network file sharing protocol that allows files, printers
and other resources to be shared between devices on a network. Originally
developed by IBM, it was adopted by Microsoft for widespread use on
Windows operating systems. SMB makes it possible for users to access, open
and edit files on different computers and use printers on the network.

The main function of SMB is to facilitate file and resource sharing between
devices on a network. For example, in an office environment, employees can
access files stored on a central server from different computers.

However, the SMB protocol can have some security vulnerabilities. In
particular, older versions contain vulnerabilities and may be susceptible to
cyber-attacks.

There are various types of access to shared resources over the SMB
protocol, such as anonymous access, guest access, authenticated access.
Anonymous access means accessing shared resources without
authentication.

Some common sharenames encountered in the SMB protocol are `C$`, `D$`,
`ADMIN$`, `IPC$`.

### C$

It is a hidden network share in Windows operating systems that gives
privileged access to system administrators. It provides access to the root
directory of the C drive.

### D$

It is a hidden share for system administrators in Windows that gives access
to the root directory of drive D.

### ADMIN$

On Windows operating systems, it is a hidden network share used for
system administration purposes. It usually provides access to the
`%WINDIR%` (for example, `C:\Windows`) directory, which is the installation
directory of Windows.

### IPC$

It stands for "Inter-Process Communication Share" and is used for inter-
process communication in Windows operating systems. This share is used for
anonymous logins and other temporary network operations over the network
and does not provide file or directory access.

### PRINT$

It is a private network share where printer drivers and printer configuration
files are stored and managed, making it easy to access and manage printers
over the network.

## Information Gathering

Let's run a port scan on our target machine

### Task 1

As can be seen in the open ports above, SMB (Server Message Block)
service is running on port 445.

## System Access

Let's try to access resources through the SMB service running on the target
machine.

### Task 2

To complete this task, we need to list the files and folders shared via the
SMB service. For this we can use the `smbclient` tool.

### smbclient

It is an FTP-like client used to access SMB resources on servers

```bash
smbclient [options] <netbios-name|ip-address>
```

- `--no-pass` — should be used when accessing a resource that does not
  require a password. If this parameter is not specified, the client will
  ask for a password.
- `-L` — this option lists which resources are available on a server.

As can be seen in the command output above, the name of the resource
containing the comment "Looks Interesting" is Projects.

### Task 3

The following command string can be used to connect to an SMB resource or
service without a password.

```bash
smbclient --no-pass \\\\<netbios-name|ip-address>\\<sharename>
```

After connecting to a source as above, we can get information about the
commands we can run with the `help` command.

### Task 4

We can use the `l` command to list the files and folders in the Projects
resource.

```bash
l
```
