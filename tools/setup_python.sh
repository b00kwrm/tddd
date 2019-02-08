sudo apt-get build-dep python3.5
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar xzvf Python-3.7.2.tgz
cd Python-3.7.2
./configure --with-openssl=/usr/local/ssl
sudo make
sudo make install

