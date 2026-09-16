# Server-Side Request Forgery (SSRF)
> **Category:** Server-Side Request Forgery · **Source:** [![PortSwigger](https://img.shields.io/badge/PortSwigger-Web_Security_Academy-FF6633?logo=portswigger&logoColor=white)](https://portswigger.net/web-security/ssrf)

Notes and solved labs on server-side request forgery — making the server issue requests on the attacker's behalf, reaching `localhost` and internal back-end systems that sit behind the firewall.

## Notes

1. [[00_Server-Side Request Forgery]] — Section overview.
2. [[01_What is SSRF?]] — Definition and the attacker → website → internal system picture.
3. [[02_What is the impact of SSRF attacks?]] — Unauthorized actions, data access, and onward attacks.
4. [[03_Common SSRF attacks]] — Attacks against the server (`localhost`) and against other back-end systems.

## Labs

| Lab | Difficulty | Key Technique |
|---|---|---|
| [[Basic SSRF against the local server]] | ![Apprentice](https://img.shields.io/badge/Apprentice-2ea44f) | Point `stockApi` at `http://localhost/admin` to delete `carlos` |

### Up next

| Lab | Key Technique |
|---|---|
| [Basic SSRF against another back-end system](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system) | Scan the `192.168.0.x` range through `stockApi` to find the internal admin interface |

## References

- [PortSwigger Web Security Academy — Server-side request forgery (SSRF)](https://portswigger.net/web-security/ssrf)

## Status

In progress. Stopped at: **SSRF attacks against other back-end systems** — next lab is *Basic SSRF against another back-end system*.
