#!/usr/bin/python3 -B
from .fernetenc import FernetEnc, FernetEncGUI

def main():
	fernetenc = FernetEnc()
	fernetenc_gui = FernetEncGUI(fernetenc)
	fernetenc_gui.run()

if __name__ == '__main__':
	raise SystemExit(main())