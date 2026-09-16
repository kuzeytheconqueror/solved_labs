# Lab: Reflected XSS into HTML Context with Nothing Encoded
> **Platform:** PortSwigger Web Security Academy · **Difficulty:** Apprentice · **Topics:** Reflected XSS

## Description

This lab contains a simple reflected cross-site scripting vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that calls the `alert` function.

## Notes

Fairly basic. The application does not control or encode the reflected data, so you can inject and run a script directly.

## Solution

1. Copy and paste the following into the search box:

	```html
	<script>alert(1)</script>
	```

2. Click **Search**.

## Reference

- [PortSwigger — Reflected XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded)
- Related notes: [[11_What is Reflected XSS]]
