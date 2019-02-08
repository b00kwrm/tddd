export LDFLAGS="-L/usr/local/ssl/lib"
export LD_LIBRARY_PATH="/usr/local/ssl/"
export CPPFLAGS="-I/usr/local/ssl/include -I/usr/local/ssl/include"
sudo apt-get build-dep python3.5
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar xzvf Python-3.7.2.tgz
cd Python-3.7.2
./configure --with-openssl=/usr/local/ssl
sudo make
sudo make install

