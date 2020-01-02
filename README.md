# Poppy
Poppy helps to [delete your Facebook](https://youtu.be/k_Jq38JKN3A).

If you are contacted on Messenger, a farewell message is displayed and further communications from this contact is blocked. One by one, every contact will be shown a farewell message and blocked until Facebook effectively is a true digital desert, it carefully wants to disguise. [For the plants!](https://youtu.be/ayfBf2J-Qlc)

![Delete your Facebook!](/poppy.jpg)

# Install/test run

Tried once on Ubuntu 18.04.1 and Raspbian 9.3, now running on Ubuntu 18.04.3.

```
sudo apt install python3-setuptools python3-bs4
git clone https://github.com/kapi2289/fbchat.git
pip3 install fbchat
git clone https://github.com/tulir/fbchat-asyncio.git
pip3 install fbchat-asyncio
wget https://raw.githubusercontent.com/boamaod/poppy/master/pop.py
chmod +x pop.py
sudo apt install screen
screen -d -m -L -U -S poppy ./pop.py
```
![You were no 15 blocked!](/block.png)
