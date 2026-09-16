# Reflected Cross-Site Scripting
> **Category:** Cross-Site Scripting (XSS) · **Source:** [PortSwigger Web Security Academy](https://portswigger.net/web-security/cross-site-scripting)

Reflected XSS is the simplest variety of cross-site scripting. It arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way.

Here is a simple example of a reflected XSS vulnerability. The request:

```
https://insecure-website.com/status?message=All+is+well.
```

is echoed straight back in the response:

```html
<p>Status: All is well.</p>
```

The application doesn't perform any other processing of the data, so an attacker can easily construct an attack like this:

```
https://insecure-website.com/status?message=<script>/*+Bad+stuff+here...+*/</script>
```

```html
<p>Status: <script>/* Bad stuff here... */</script></p>
```

If the user visits the URL constructed by the attacker, then the attacker's script executes in the user's browser, in the context of that user's session with the application. At that point, the script can carry out any action, and retrieve any data, to which the user has access.

> Deeper dive: [[11_What is Reflected XSS]]
