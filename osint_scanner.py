
import socket
import requests
import whois
import dns.resolver


def osint_scan(domain):
    domain = domain.strip().lower()

    print("\n" + "=" * 55)
    print("           OSINT DOMAIN INFORMATION")
    print("=" * 55)
    print("Domain:", domain)

    # 1. Domain registration information
    print("\n[1] DOMAIN REGISTRATION")

    try:
        data = whois.whois(domain)

        fields = {
            "Registrar": data.registrar,
            "Creation Date": data.creation_date,
            "Updated Date": data.updated_date,
            "Expiry Date": data.expiration_date,
            "Domain Status": data.status,
            "Name Servers": data.name_servers,
        }

        for key, value in fields.items():
            print(f"{key}: {value if value else 'Unavailable'}")

    except Exception as error:
        print("WHOIS lookup failed:", error)

    # 2. IP address resolution
    print("\n[2] IP ADDRESSES")

    try:
        addresses = sorted({
            item[4][0]
            for item in socket.getaddrinfo(
                domain, None, type=socket.SOCK_STREAM
            )
        })

        for address in addresses:
            print(address)

    except socket.gaierror as error:
        print("IP lookup failed:", error)
        addresses = []

    # 3. DNS record collection
    print("\n[3] DNS RECORDS")

    for record_type in ["A", "AAAA", "MX", "NS", "TXT", "CAA"]:
        try:
            answers = dns.resolver.resolve(
                domain, record_type, lifetime=5
            )

            print(f"\n{record_type} Records:")

            for answer in answers:
                print(" ", answer)

        except Exception:
            print(f"{record_type}: No result or lookup failed")

    # 4. IP geolocation
    print("\n[4] IP GEOLOCATION")

    if addresses:
        try:
            # Use the first resolved IP for this lookup.
            ip = addresses[0]

            response = requests.get(
                f"https://ipwho.is/{ip}",
                timeout=10
            )
            response.raise_for_status()
            geo = response.json()

            if geo.get("success"):
                print("IP:", ip)
                print("Country:", geo.get("country"))
                print("Region:", geo.get("region"))
                print("City:", geo.get("city"))
                print(
                    "ISP:",
                    geo.get("connection", {}).get("isp")
                )
            else:
                print("Geolocation unavailable")

        except requests.RequestException as error:
            print("Geolocation request failed:", error)

    print("\nOSINT collection completed.")


if __name__ == "__main__":
    target = input("Enter domain (e.g. example.com): ")
    osint_scan(target)

