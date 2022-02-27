# Fernet Encryption
Python app for encrypting messages with fernet cryptography. This tool is primarily intended for Linux, but works on Windows and Mac using the Git Bash (https://git-scm.com/downloads).
* Github repo: https://github.com/ArcticTechnology/FernetEncryption
* PyPi: https://pypi.org/project/FernetEncryption/

## Prerequisites
The Fernet Encryption app is intended for the Linux terminal and should work on it out of the box. However, you may need to add ```~/.local/bin/``` to PATH if you are getting a ```command not found``` error when trying to run the app. See this thread for details: https://stackoverflow.com/a/34947489. To add ```~/.local/bin/``` to PATH do the following:
1. Add ```export PATH=~/.local/bin:$PATH``` to ```~/.bash_profile```.
```
echo export PATH=~/.local/bin:$PATH > ~/.bash_profile
````
2. Execute command.
```
source ~/.bash_profile
```

This app can work for Windows and Mac. It is recommended to run it on the Git Bash terminal. Here are the instructions for installing and setting up Git Bash:

1. Go to https://git-scm.com/downloads and click download.
```
Version >= 2.34.1
```
2. During the installation setup, make sure to include OpenSSH. Recommenced setting should be fine:
```
Use bundled OpenSSH - This uses ssh.exe that comes with Git.
```
3. Leave the other settings as default, click through, and install.

IMPORTANT: For Windows, run this app on the ```bash.exe``` terminal rather ```git-bash.exe```. There is a known issue with ```git-bash.exe``` messing up Python ```os``` commands in ```import os```. See this thread for details: https://stackoverflow.com/questions/33622087/composer-installation-error-output-is-not-a-tty-input-is-not-a-tty/33623136#33623136.
* ```bash.exe``` can be found in your Git folder in the ```bin/``` directory.
* For example: If ```git-bash.exe``` is here ```C:\Program Files\Git\git-bash.exe``` then you should find ```bash.exe``` here ```C:\Program Files\Git\bin\bash.exe```.

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

![alt text](https://github.com/ArcticTechnology/BitcoinAddresses/blob/main/btcaddr1.png?raw=true)
