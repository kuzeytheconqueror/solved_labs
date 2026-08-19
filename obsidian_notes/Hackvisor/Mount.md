# Mount

> **Platform:** Hackvisor · **Difficulty:** Warmup · **Topics:** NFS, Misconfiguration, File Sharing, Mounting Exports

## Introduction
Mount warmup is an ideal starting point for basic exercises with the NFS
service. On this machine, you will learn how to access sensitive files on
remote computers through a vulnerability caused by misconfiguration of the
NFS service. You will also learn the basics of how NFS works and how to
connect to it.

## Network File Sharing (NFS)
Network File System (NFS) is a file-based network protocol that allows users
to access files on different systems as if they were on their local disk.
Developed in 1984 by Sun Microsystems, NFS is widely used on Unix-based
systems, but is also supported by Windows and other operating systems.
NFS simplifies the exchange of data between different computers by
facilitating file sharing on a network.

## Information Gathering
Let's start collecting information by running a port scan on our target
machine.

## Task 1
As a result of our port scan, we found that the service running on port 2049
is nfs.

## Task 2
NFS stands for Network File Sharing.

## Task 3
The command used to display NFS exports is `showmount`.

## System Access

## Task 4
Let's view NFS exports using the following command.
```bash
showmount -e <target-ip>
```

- `-a` — List both the client computer name or IP address and the mounted
  directory in computer:directory format.
- `-d` — List only the mounted directories.
- `-e` — Show the export list of the NFS server.
- `-h` — Help menu.

We found that the path to the shared export is `/root`.

## Task 5
We can use the `mount` command to mount NFS exports to our own
computer.

- `-t` — Limits the set of file system types.
- `-o` — Used to specify a comma-separated list of mount options.
- `-l` — Also shows file system tags.

## Task 6
We need to mount the export on our own computer to access the password
information requested in the task. To do this, first create a folder under the
`/mnt` directory using the `mkdir` command.

```bash
mkdir /mnt/nfs_mount
```

Then let's mount the export to the `nfs_mount` folder we created on our
computer using the following command.

```bash
mount -t nfs <target-ip>:/root /mnt/nfs_mount/
```
