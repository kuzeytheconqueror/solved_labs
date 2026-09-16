# Lab: DOM XSS in document.write Sink Using Source location.search
> **Platform:** PortSwigger Web Security Academy · **Difficulty:** Apprentice · **Topics:** DOM-Based XSS, document.write

## Description

This lab contains a DOM-based cross-site scripting vulnerability in the search query tracking functionality. It uses the JavaScript `document.write` function, which writes data out to the page. The `document.write` function is called with data from `location.search`, which you can control using the website URL.

To solve the lab, perform a cross-site scripting attack that calls the `alert` function.

## Solution

1. Enter a random alphanumeric string into the search box.
2. Right-click and inspect the element, and observe that your random string has been placed inside an `img src` attribute.
3. Break out of the `img` attribute by searching for:

	```html
	"><svg onload=alert(1)>
	```

## Reference

- [PortSwigger — DOM XSS in document.write sink using source location.search](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)
- Related notes: [[33_Exploiting DOM XSS with different sources and sinks]]
