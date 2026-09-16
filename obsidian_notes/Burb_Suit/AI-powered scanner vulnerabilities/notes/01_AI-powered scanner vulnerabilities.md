# AI-Powered Scanners — Overview
> **Category:** Web LLM Attacks · **Source:** [PortSwigger Web Security Academy](https://portswigger.net/web-security/llm-attacks/ai-powered-scanner-vulnerabilities)

Application security teams often deploy AI-powered scanners that use Large Language Models (LLMs) to scan web applications for vulnerabilities.

While designed to improve security testing efficiency, these agents introduce a new attack surface. If a scanner can be influenced by attacker-controlled content, it may be manipulated into performing unintended actions, accessing internal resources, or exfiltrating sensitive information.

In this section, we'll explore how these agents operate and the techniques that can be used to compromise the scanning environment.

## What are AI-powered web application security scanners?

AI-powered scanners are web security testing tools that combine traditional crawling and request generation with LLM-driven reasoning. Like traditional Dynamic Application Security Testing (DAST) scanners, they can:

- Authenticate as users.
- Crawl applications.
- Send HTTP requests.
- Chain multiple actions.

### Traditional vs. AI-powered scanners

The key difference between traditional and AI-powered scanners is how decisions are made.

Traditional scanners use a rigid, instruction-based architecture. Because these tools lack semantic understanding, they cannot "read" a page to determine its purpose. Instead, they rely on pattern matching and known vulnerability signatures.

In contrast, AI-powered scanners replace rigid logic with autonomous reasoning. Rather than following a static script, these tools use LLMs to interpret web content and plan their next actions.

Some key behaviors of AI-powered scanners from a security perspective include:

- **Using LLM reasoning to decide what to test next**. They evaluate the state of the application to determine a logical next step.
- **Interpreting application responses semantically**. They "read" the text in a response to understand its context, enabling them to identify complex business logic that a traditional scanner might ignore.
- **Selecting tools and constructing requests based on model output**. Some AI scanners use "tool-calling" capabilities to interact with APIs, databases, or UI elements based on their own internal reasoning.
