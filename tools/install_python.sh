sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar xzvf Python-3.7.2.tgz
cd Python-3.7.2
./configure
sudo make
sudo make install
cd ~/
/usr/local/bin/python3.7 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
