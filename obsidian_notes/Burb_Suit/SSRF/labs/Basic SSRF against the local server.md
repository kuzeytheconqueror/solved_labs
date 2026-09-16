# Lab: Basic SSRF Against the Local Server
> **Platform:** PortSwigger Web Security Academy · **Difficulty:** Apprentice · **Topics:** SSRF, Access Control Bypass

## Description

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user `carlos`.

## Notes

The stock checker takes a full URL in the `stockApi` parameter and fetches it server-side. Anything the server can reach, we can reach through it — including `/admin`, which is blocked when requested directly but trusted when the request comes from `localhost`.

## Solution

1. Browse to `/admin` and observe that you can't directly access the admin page.
2. Visit a product, click **Check stock**, intercept the request in Burp Suite, and send it to Burp Repeater.
3. Change the URL in the `stockApi` parameter to:

	```text
	stockApi=http://localhost/admin
	```

	This should display the administration interface.

4. Read the HTML to identify the URL to delete the target user, which is:

	```text
	http://localhost/admin/delete?username=carlos
	```

5. Submit this URL in the `stockApi` parameter to deliver the SSRF attack.

## Reference

- [PortSwigger — Basic SSRF against the local server](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost)
- Related notes: [[03_Common SSRF attacks]]
