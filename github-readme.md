# Active Directory Attack Lab

A self-built Active Directory environment used to practice real-world attacker techniques — enumeration, password spraying, Kerberoasting, and BloodHound-based attack path mapping — entirely on infrastructure I own.

## Environment

- **Target:** Ubuntu 22.04 running Samba as an AD Domain Controller (`SECURECORP.LOCAL`)
- **Attacker machines:** Windows (native tools, SharpHound) and Kali Linux (Impacket)
- **Analysis stack:** BloodHound Community Edition, deployed via Docker

## Attack Chain

1. **User Enumeration** — Authenticated LDAP query via Impacket's `GetADUsers.py` to pull the full domain user list.
2. **Password Spraying** — Custom Python script (using `impacket.smbconnection`) tested a list of common weak passwords against a service account. Successfully cracked `svc_backup`.
3. **Kerberoasting** — Attempted against the compromised account; blocked by a documented Samba/Impacket compatibility issue after extensive troubleshooting (encryption types, clock sync, library versions). Noted as a known environment limitation.
4. **Privilege Verification** — Confirmed the compromised account correctly lacks domain admin rights (denied on a `secretsdump` attempt).
5. **BloodHound Mapping** — Collected full domain data with SharpHound and analyzed it in BloodHound CE. Pathfinding confirmed **no privilege escalation path** exists from the compromised account to Domain Admins.

## Key Finding

Password spraying successfully compromised a weak service account, but the domain's privilege structure correctly prevented further escalation — validated both through direct testing and BloodHound's full graph analysis.

## Tools Used

Samba AD, Impacket, Python, BloodHound CE, SharpHound, Docker, Neo4j

## What I Learned

Hands-on experience with the full attacker workflow — recon, credential attacks, and graph-based attack path analysis — plus real troubleshooting: diagnosing a DNS misconfiguration (Samba's DNS service binding to IPv6 only) that was blocking tool connectivity, and working around a genuine tool compatibility bug rather than a configuration mistake.
