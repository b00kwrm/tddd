# https://github.com/brandon-rhodes/fopnp/blob/2c1d0fcb97560394d0fa52eead317567b1f02504/py3/chapter16/ssh_simple.py

import paramiko

user = 'oracle'
password = 'ginger'
hostname = '127.0.0.1'
port = 8000

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect(hostname, port=port, username=user password=password)

    

