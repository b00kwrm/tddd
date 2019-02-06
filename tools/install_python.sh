sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install build-essential checkinstall libbz2-dev libc6-dev libgdbm-dev libncursesw5-dev libreadline-gplv2-dev libssl-dev libsqlite3-dev tk-dev openssl libtemplate-perl zlib1g-dev
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar xzvf Python-3.7.2.tgz
cd Python-3.7.2
./configure --enable-optimizations >> conf_script.txt
sudo make
sudo make altinstall
cd ..
wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz
tar xzvf Python-3.6.6.tgz
cd Python-3.6.6
./configure --enable-optimizations >> conf_script.txt
make
sudo make altinstall
cd ~/repo
/usr/local/bin/python3.6 -m venv venv
. venv/bin/activate
pip install -r requirements.txt


