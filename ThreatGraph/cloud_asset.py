import dns.resolver

domain = input("Domain: ")

records = ["A","AAAA","MX","TXT","NS","CNAME"]

for r in records:

    try:

        answers = dns.resolver.resolve(domain,r)

        print(f"\n[{r}]")

        for answer in answers:
            print(answer)

    except:
        pass
