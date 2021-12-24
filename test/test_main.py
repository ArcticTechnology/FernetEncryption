#!/usr/bin/python3 -B
from fernetencryption import *

def test_main():
	fernetenc = FernetEnc()
	fernetenc_gui = FernetEncGUI(fernetenc)
	fernetenc_gui.run()

if __name__ == '__main__':
	raise SystemExit(test_main())