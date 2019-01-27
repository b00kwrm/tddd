# https://github.com/brandon-rhodes/fopnp/blob/2c1d0fcb97560394d0fa52eead317567b1f02504/py3/chapter16/ssh_simple.py

import paramiko
import time

user = 'oracle'
password = 'ginger'
hostname = '127.0.0.1'
port = 8000

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect(hostname, port=port, username=user, password=password)
stdin, stdout, stderr = client.exec_command('ps aux')
client.close()

time.sleep(5)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect(hostname, port=port, username=user, password=password)
stdin, stdout, stderr = client.exec_command('lsmod')
client.close()

time.sleep(5)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect(hostname, port=port, username=user, password=password)
stdin, stdout, stderr = client.exec_command('cat /etc/passwd')
client.close()

time.sleep(5)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect(hostname, port=port, username=user, password=password)
stdin, stdout, stderr = client.exec_command('wget http://www.gnu.org')
client.close()


