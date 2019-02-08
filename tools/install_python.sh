LD_LIBRARY_PATH=/usr/local/ssl
export LD_LIBRARY_PATH
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get build-dep openssl
sudo apt-get build-dep python3.5
wget https://www.openssl.org/source/openssl-1.0.2q.tar.gz
tar xzvf openssl-1.0.2q.tar.gz
cd openssl-1.0.2q
sudo ./config
sudo make
sudo make install
sudo mv /usr/bin/openssl /usr/bin/openssl_ORIG
sudo ln -sf /usr/local/ssl/bin/openssl `which openssl`
cd ..
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar xzvf Python-3.7.2.tgz
cd Python-3.7.2
./configure --with-openssl=/usr/local/ssl
sudo make
sudo make install
cd /home/circleci/repo
/usr/local/bin/python3.7 -m venv venv
. venv/bin/activate
pip install -r requirements.txt


