# Fernet Encryption
Python app for encrypting messages with fernet cryptography. This tool is primarily intended for Linux, but works on Windows and Mac using the Git Bash (https://git-scm.com/downloads).
* Github repo: https://github.com/ArcticTechnology/FernetEncryption
* PyPi: https://pypi.org/project/FernetEncryption/

## Installation
This library is hosted on PyPi and can be installed via ```pip```:
```
pip3 install FernetEncryption
```

## Usage
The purpose of this app is to provide an easy way to fernet to create encrypted messages.

After installation, you can run this app in your terminal with this command:
```
fernetencryption
```
You can also run this app with ```python3 -m```:
```
python3 -m fernetencryption
```
The interface is quite simple. Encrypt lets you encrypt a message with a password. Decrypt lets you decrypt a fernet encrypted message with its associated password.

You can import the package resources and run them in your own project:
```
from fernetencryption import *
fernetenc = FernetEnc()
fernetenc_gui = FernetEncGUI(fernetenc)
fernetenc_gui.run()
```

## Support and Contributions
Our software is open source and free for public use. If you found any of these repos useful and would like to support this project financially, feel free to donate to our bitcoin address.

Bitcoin Address 1: 1GZQY6hMwszqxCmbC6uGxkyD5HKPhK1Pmf

![alt text](https://github.com/ArcticTechnology/BitcoinAddresses/blob/master/btcaddr1.png?raw=true)
