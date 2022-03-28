# Fernet Encryption
Python app for encrypting messages with fernet cryptography. This tool is primarily intended for Linux and Mac, but works on Windows using the Git Bash (https://git-scm.com/downloads).
* Github repo: https://github.com/ArcticTechnology/FernetEncryption
* PyPi: https://pypi.org/project/FernetEncryption/

## Prerequisites
For Windows, it is recommended to run this app on a Linux emulation layer such as the Git Bash terminal. See the "Instructions for Git Bash" section for details. In addition to Git Bash you will also need to install Python3 and Pip3 as described below.

For Mac and Linux, this app should work out of the box on the Linux or Mac terminal, but you must have Python3 and Pip3 as described below.

This app requires the following:
* Python3 (version 3.8 or greater) - Install Python3 here: [https://www.python.org/downloads/]. Check version with: ```python3 --version```.
* Pip3 (version 20.2.1 or greater) - Make sure to install python3-pip in order to use pip install. Check version with: ```pip3 --version```.

## Installation
There are a couple of options to install this app:
* Pip Install - This app is hosted on PyPi and can be installed with the following command:
```
pip3 install FernetEncryption
```
* Local Install - Alternatively, you can download or git clone the Github repo and install it locally with the following:
```
git clone https://github.com/ArcticTechnology/FernetEncryption.git
cd FernetEncryption
pip3 install -e .
```
To uninstall this app:
```
pip3 uninstall FernetEncryption
```
* If you used the local install option, you will also want to delete the ```.egg-info``` file located in the ```src/``` directory of the package. This gets created automatically with ```pip3 install -e .```.

## Usage
After installation, you have a couple ways to run this app.
* Run this app from the terminal with this command:
```
fernetencryption
```
* Run this app with the python command ```python3 -m```:
```
python3 -m fernetencryption
```
* You can also import the package resources and run them in your own project:
```
from fernetencryption import *
fernetenc = FernetEnc()
fernetenc_gui = FernetEncGUI(fernetenc)
fernetenc_gui.run()
```

## Troubleshooting
This section goes over some of the common issues found and how to resolve them.

### "Command Not Found" Error When Running the App
On Linux, if you are getting a ```command not found``` error when trying to run the app, you may need to add ```~/.local/bin/``` to PATH. See this thread for details: [https://stackoverflow.com/a/34947489]. To add ```~/.local/bin/``` to PATH do the following:

1. Add ```export PATH=~/.local/bin:$PATH``` to ```~/.bash_profile```.
```
echo export PATH=~/.local/bin:$PATH > ~/.bash_profile
```
2. Execute command.
```
source ~/.bash_profile
```

### Instructions for Git Bash
For Windows, it is recommended to run this app on a linux emulation layer like the Git Bash terminal. Here are the instructions for installing and setting up Git Bash:
1. Go to https://git-scm.com/downloads and click download.
```
Version >= 2.34.1
```
2. During the installation setup, make sure to include OpenSSH. Recommenced setting should be fine:
```
Use bundled OpenSSH - This uses ssh.exe that comes with Git.
```
3. Leave the other settings as default, click through, and install.
4. Open ```bash.exe``` and install Python3 https://www.python.org/downloads/
5. Proceed to the "Installation" section to install this app.

IMPORTANT: For Windows, use the ```bash.exe``` terminal rather ```git-bash.exe```. There is a known issue with ```git-bash.exe``` messing up Python ```os``` commands in ```import os```. See this thread for details: [https://stackoverflow.com/a/33623136].
* You can find ```bash.exe``` Git folder in the ```bin/``` directory. For example: If ```git-bash.exe``` is here ```C:\Program Files\Git\git-bash.exe``` then you should find ```bash.exe``` here ```C:\Program Files\Git\bin\bash.exe```.

## Support and Contributions
Our software is open source and free for public use. If you found any of these repos useful and would like to support this project financially, feel free to donate to our bitcoin address.

Bitcoin Address 1: 1GZQY6hMwszqxCmbC6uGxkyD5HKPhK1Pmf

![alt text](https://github.com/ArcticTechnology/BitcoinAddresses/blob/main/btcaddr1.png?raw=true)