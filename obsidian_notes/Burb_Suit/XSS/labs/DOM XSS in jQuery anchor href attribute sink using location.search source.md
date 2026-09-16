# Lab: DOM XSS in jQuery Anchor href Attribute Sink Using location.search Source
> **Platform:** PortSwigger Web Security Academy · **Difficulty:** Apprentice · **Topics:** DOM-Based XSS, jQuery

## Description

This lab contains a DOM-based cross-site scripting vulnerability in the submit feedback page. It uses the jQuery library's `$` selector function to find an anchor element, and changes its `href` attribute using data from `location.search`.

To solve the lab, make the **back** link alert `document.cookie`.

## Solution

1. On the **Submit feedback** page, change the query parameter `returnPath` to `/` followed by a random alphanumeric string.
2. Right-click and inspect the element, and observe that your random string has been placed inside the anchor's `href` attribute.
3. Change `returnPath` to:

	```
	javascript:alert(document.cookie)
	```

4. Press Enter and click **back**.

## Reference

- [PortSwigger — DOM XSS in jQuery anchor href attribute sink using location.search source](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-href-attribute-sink)
- Related notes: [[33_Exploiting DOM XSS with different sources and sinks]]
