# Lab: Stored XSS into HTML Context with Nothing Encoded
> **Platform:** PortSwigger Web Security Academy · **Difficulty:** Apprentice · **Topics:** Stored XSS

## Description

This lab contains a stored cross-site scripting vulnerability in the comment functionality.

To solve the lab, submit a comment that calls the `alert` function when the blog post is viewed.

## Notes

A basic lab. The submitted inputs are not encoded or controlled, so they are easy to manipulate into a stored payload.

## Solution

1. Enter the following into the comment box:

	```html
	<script>alert(1)</script>
	```

2. Enter a name, email, and website.
3. Click **Post comment**.
4. Go back to the blog.

## Reference

- [PortSwigger — Stored XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded)
- Related notes: [[21_Stored XSS]]
