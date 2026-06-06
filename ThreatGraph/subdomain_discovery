import os

DOMAIN = input("Enter Domain:").strip()

subdomains_file = "chess.txt"
live_hosts_file = "live_hosts.txt"

# Read subdomains
subdomains = []
if os.path.exists(subdomains_file):
    with open(subdomains_file, "r") as f:
        subdomains = [line.strip() for line in f if line.strip()]

# Read live hosts
live_hosts = []
if os.path.exists(live_hosts_file):
    with open(live_hosts_file, "r") as f:
        live_hosts = [line.strip() for line in f if line.strip()]

# Display Summary
print("\n" + "=" * 40)
print("      ThreatGraph Scan Summary")
print("=" * 40)

print(f"\nTarget Domain: {DOMAIN}")

print(f"\nSubdomains Found: {len(subdomains)}")
print(f"Live Hosts Found: {len(live_hosts)}")

print("\nLive URLs:")
print("-" * 40)

if live_hosts:
    for host in live_hosts:
        print(host)
else:
   print("No live hosts found.")

print("\n" + "=" * 40)
print("Scan Completed")
print("=" * 40)


