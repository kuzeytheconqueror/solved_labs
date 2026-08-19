# File Hunter

> **Platform:** Hackvisor · **Difficulty:** Warmup · **Topics:** FTP, Anonymous Login, Enumeration

## What is FTP?
FTP (File Transfer Protocol) is a network protocol for transferring files over
the internet. Developed in 1971, it allows users to upload files to or
download files from servers. FTP is particularly useful for managing websites
and sharing data.

FTP usually consists of two basic components: an FTP server and an FTP
client. The FTP server is a centralized computer where files are stored and
made available to the outside world. The FTP client is the software that
allows users to connect to the FTP server and transfer files. Users usually
connect to the FTP server using a username and password, but some servers
may also allow anonymous access.

FTP continues to be popular due to its ease of use and wide compatibility.
However, the fact that FTP is an unencrypted protocol carries some risks for
data security. For this reason, SFTP (SSH File Transfer Protocol) or FTPS
(FTP Secure) is often preferred as a secure alternative for transferring
sensitive data.

The following command string is used to connect to an FTP server:

```bash
ftp <SERVER-IP-ADDRESS> -P <PORT-NUMBER>
```

Note: We don't need to specify a port number when connecting if the FTP
service uses port 21 by default.

```bash
ftp 190.2.3.4
```

In the example above we can see how we can connect anonymously to an
FTP server.

After connecting to an FTP server, we use the `help` command to see the
commands we can run. Below you can see some important commands.

- `help` — Shows the commands that can be run and gives information about the commands.
- `get` — Used to get a file.
- `dir` — Lists the contents of a remote directory.
- `bye` — End the FTP session and exit.

## Information Gathering
Let's run a port scan for our target machine.

### Task 1
To learn the version information of the services, we add the `-sV` parameter
to our `nmap` command.

```bash
nmap -sV 190.2.3.4
```

### Task 2

FTP stands for File Transfer Protocol, as explained earlier in this article.

## System Access
Let's try to connect to our target machine with FTP.

```bash
ftp 172.20.24.150
```

### Task 3
When trying to connect to FTP, we see a welcome message without entering a username and password yet. As we can see from this message, let's try to connect to the FTP services anonymously.
**Note**: It just writes `anonymous` and that's all for the FTP.

Yes, we have successfully connected to the server anonymously.

Anonymous FTP access allows anyone to access specific files on the server
without requiring a username and password. This is often used for the
distribution of open source software, public data or big files.

To connect anonymously to an FTP server, one connects to the server
address via the FTP client, usually by typing "anonymous" in the username
field and keeping the password field blank. Once the connection is
established, users can view and download files from the server.

Anonymous FTP provides easy accessibility and makes it easier to share
information. However, for security reasons, server owners also need to
carefully manage the accessible content.

### Task 4
Run the `help` command at the FTP server.

```bash
help
```

### Task 5
Run the `ls` command.

```bash
ls
```

### Task 6
We can use the `get` command that we see in the command list to download files.

```bash
help get
```

### Task 7

We can download the `userlist` file on the FTP server with the `get` command
and close the FTP connection. Then we just need to read the contents of the
file with the `cat` command.

```bash
get userlist
```

`userlist` is the file, so that's all.
