# Reddict

> **Platform:** Hackvisor · **Difficulty:** Warmup · **Topics:** Redis, NoSQL, Enumeration

## Introduction

The Reddict warmup machine is the ideal starting point for learning about
the security of NoSQL databases. In Reddict, you will learn how to detect
and exploit vulnerabilities in Redis services, while also learning about the
basic operation and configuration of Redis. This experience will give you a
perspective on NoSQL database security and help you improve your
cybersecurity skills.

## NoSQL

NoSQL is a type of database management system that offers more flexible
data models instead of the strict schemas and query languages of traditional
relational database systems. The name originated as an abbreviation of "Not
Only SQL", which means that NoSQL systems support different data storage
and query methods other than SQL.

NoSQL databases are designed to work with unstructured data on a large
scale and thus meet the needs of large-scale, distributed applications. These
systems typically offer features such as high performance, horizontal
scalability and easy data distribution.

## Redis

Redis (REmote DIctionary Service) is an open source, speed-oriented and
high-performance database management system. First developed in 2009,
Redis is especially known for its key-value storage structure and supports a
wide variety of data types. These data types include arrays, lists, maps, sets
and ordered sets. Its performance is high because it stores data in memory
and writes it to disk when needed. With these features, Redis offers an ideal
solution for situations such as session management, caching, message
queues and real-time applications, especially in web applications.

One of the most remarkable features of Redis is that it has a simple and
effective structure. It also stands out with its easy scalability and use in
distributed systems. It also has features such as replication and key
expiration to ensure high availability and durability. With its fast and flexible
structure, Redis is often preferred by developers and system administrators
who want to perform high-performance operations on large data sets.
Therefore, it has become a popular component in modern application
architectures.

## Redis-cli

`redis-cli` is a command line tool used to manage and interact with the Redis
database system. This tool facilitates operations such as adding, updating
and retrieving data and managing database configuration by communicating
directly with Redis servers.

### Syntax

```bash
redis-cli -h <hostname> -p <port-number> --user <username> -a <password>
```

- `-h` — The hostname or IP address of the computer running the Redis server to connect to.
- `-p` — The parameter used to specify the port number. It is not necessary to specify if you want to connect to Redis's default port 6379.
- `--user` — Used to specify which user to connect as when connecting to the Redis server.
- `-a` — Parameter used to specify a password.

### Example Connection

In the example connection below, there is no need to use parameters such
as hostname as it connects to the Redis server on the computer (local)
where the `redis-cli` tool is running.

```bash
redis-cli
```

### PING

Checks if the redis server is running.

```bash
redis-cli
```

### Help

Provides Information about the commands

```bash
HELP PING
```

### INFO

provides information and statistics about the server.

```bash
INFO
```

### Monitor

Listens for all requests received by the server in real time.

```bash
MONITOR
```

### SET

set the string value of a key

```bash
SET example_key "example_value"
```

### GET

get the value of a key

```bash
GET example_key
```

### KEYS

Find all keys matching the given pattern.

```bash
KEYS *
```

### QUIT

Close the connection.

```bash
QUIT
```

## Information Gathering

Let's run a port scan for our target machine.

## Task 1, Task 2

```bash
nmap -sV -p1-10000 <the ip>
```

## System Access

Let's try to connect to the redis server running on our target machine.

## Task 3, Task 4

We can use the `redis-cli` tool to connect to a remote redis server.

```bash
redis-cli -h 172.20.1.26
```

## Task 5, Task 6, Task 7

The `INFO` command is used to get information and statistics about the Redis
server.

The `KEYS *` command is used to display all keys.

## Task 8, Task 9

The `GET` command is used to display the value of a key.

In Task 9, let's look at the value of the `session:admin-001` key since it
asks for admin session information
