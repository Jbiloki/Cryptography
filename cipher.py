#!bin/usr/python3
import sys
import playfair
import caesar
import railfence
import vigenre
def main():
	args = str(sys.argv)
	if(sys.argv[1] == "PLF"):
		cipher = playfair.Play()
		if(cipher.setKey(sys.argv[2])):
			cipherText = "flalrbrnqcgwcsogqn"
			if(sys.argv[3] == "ENC"):
				cipher.encrypt(cipherText)
			if(sys.argv[3] == "DEC"):
				cipher.decrypt(cipherText)
		else:
			print('Key Undefined')
	if(sys.argv[1] == "CES"):
		cipher = caesar.Caesar()
		if(cipher.setKey(sys.argv[2])):	
			if(sys.argv[3] == "ENC"):
				cipher.encrypt(cipherText)
			if(sys.argv[3] == "DEC"):
				cipher.decrypt(cipherText)
		else:
			print('Key Undefined')
	if(sys.argv[1] == "RFC"):
		cipher = railfence.Rail()
		if(cipher.setKey(sys.argv[2])):
			cipherText = "cpeeriourciemtsuts"	
			if(sys.argv[3] == "ENC"):
				cipher.encrypt(cipherText)
			if(sys.argv[3] == "DEC"):
				cipher.decrypt(cipherText)
		else:
			print('Key Undefined')
	if(sys.argv[1] == "VIG"):
		cipher = vigenre.Vigenre()
		if(cipher.setKey(sys.argv[2])):	
			cipherText = "zicvtwqngrzgvtwavzhcqyglmgj"
			if(sys.argv[3] == "ENC"):
				cipher.encrypt(cipherText)
			if(sys.argv[3] == "DEC"):
				cipher.decrypt(cipherText)
		else:
			print('Key Undefined')


main()
