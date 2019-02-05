from pexpect import pxssh

user = "oracle"
password = "ginger"
hostname = "127.0.0.1"

s = pxssh.pxssh(
    options={"StrictHostKeyChecking": "no", "UserKnownHostsFile": "/dev/null"}
)

s.login(hostname, user, password=password, port=8000)
s.sendline("uptime")
s.prompt()
print(s.before)
s.sendline("ps auxf")
s.prompt()
print(s.before)
s.sendline("lsmod")
s.prompt()
print(s.before)
s.sendline('echo "w" >> .bashrc')
s.prompt()
print(s.before)
s.logout()
