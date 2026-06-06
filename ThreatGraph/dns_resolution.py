import subprocess
import dns.resolver

domain = input("Enter Domain: ").strip()

print("\n[+] Running Subfinder...\n")

result = subprocess.run(
    ["subfinder", "-d", domain, "-silent"],
    capture_output=True,
    text=True
)

subdomains = result.stdout.splitlines()

print(f"[+] Found {len(subdomains)} subdomains\n")

resolved_results = []

for subdomain in subdomains:
    try:
        answers = dns.resolver.resolve(subdomain, "A")
        ips = [answer.to_text() for answer in answers]

        resolved_results.append({
            "subdomain": subdomain,
            "ips": ips
        })

    except Exception:
        continue

print("=" * 60)
print("ThreatGraph Discovery + DNS Resolution")
print("=" * 60)

for item in resolved_results:
    print(f"\n{item['subdomain']}")

    for ip in item["ips"]:
        print(f"   └── {ip}")
