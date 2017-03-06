#!bin/usr/python3
import sys
import playfair

def main():
	args = str(sys.argv)
	if(sys.argv[1] == "PLF"):
		cipher = playfair.Play(sys.argv[2])
		cipherText = "uztbdlgzpnnwlgtgtuerovldbduhfperhwqsrz"
		if(sys.argv[3] == "ENC"):
			cipher.encrypt(cipherText)
		if(sys.argv[3] == "DEC"):
			cipher.decrypt(cipherText)
		

main()
