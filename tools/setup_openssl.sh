sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get build-dep openssl
wget https://www.openssl.org/source/openssl-1.0.2q.tar.gz
tar xzvf openssl-1.0.2q.tar.gz
cd openssl-1.0.2q
sudo ./config
sudo make
sudo make install
sudo ln -s /usr/local/ssl/bin/openssl /usr/bin/openssl
