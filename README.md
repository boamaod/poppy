# Poppy
Poppy helps to [delete your Facebook](https://youtu.be/k_Jq38JKN3A).

![Delete your Facebook!](/poppy.jpg)

# Install/test run

Tried on Ubuntu 18.04.1 and Raspbian 9.3.

```
sudo apt install python3-setuptools python3-bs4
git clone https://github.com/kapi2289/fbchat.git
cd fbchat
python3 setup.py install --user
wget https://raw.githubusercontent.com/boamaod/poppy/master/pop.py
chmod +x pop.py
sudo apt install screen
screen -dmLU -S poppy ./pop.py
```
