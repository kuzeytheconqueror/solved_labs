# Lab: DOM XSS in innerHTML Sink Using Source location.search
> **Platform:** PortSwigger Web Security Academy · **Difficulty:** Apprentice · **Topics:** DOM-Based XSS, innerHTML

## Description

This lab contains a DOM-based cross-site scripting vulnerability in the search blog functionality. It uses an `innerHTML` assignment, which changes the HTML contents of a `div` element, using data from `location.search`.

To solve the lab, perform a cross-site scripting attack that calls the `alert` function.

## Solution

1. Enter the following into the search box:

	```html
	<img src=1 onerror=alert(1)>
	```

2. Click **Search**.

The value of the `src` attribute is invalid and throws an error. This triggers the `onerror` event handler, which then calls the `alert()` function. As a result, the payload is executed whenever the user's browser attempts to load the page containing your malicious post.

## Reference

- [PortSwigger — DOM XSS in innerHTML sink using source location.search](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink)
- Related notes: [[33_Exploiting DOM XSS with different sources and sinks]]
