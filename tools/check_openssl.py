import subprocess

vers = subprocess.check_output(["openssl", "version"])

assert vers == "OpenSSL 1.0.2q  20 Nov 2018\n"
