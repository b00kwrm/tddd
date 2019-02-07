sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install build-essential checkinstall libbz2-dev libc6-dev libgdbm-dev libncursesw5-dev libreadline-gplv2-dev libssl-dev libsqlite3-dev tk-dev openssl libtemplate-perl zlib1g-dev
wget https://www.openssl.org/source/openssl-1.0.2q.tar.gz
tar xzvf openssl-1.0.2q.tar.gz
cd openssl-1.0.2q
sudo ./config
sudo make
sudo make install
mv /usr/bin/openssl /usr/bin/openssl_ORIG
sudo ln -s /usr/local/ssl/bin/openssl /usr/bin/openssl
cd ..
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar xzvf Python-3.7.2.tgz
cd Python-3.7.2
./configure
sudo make
sudo make install
cd /home/circleci/repo
/usr/local/bin/python3.7 -m venv venv
. venv/bin/activate
pip install -r requirements.txt


