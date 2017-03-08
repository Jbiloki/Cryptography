#!/usr/bin/python3

class Vigenre:

	def __init__(self):
		self.key = None
		return

	def setKey(self, key):
		if(any(char.isdigit() for char in key) == False):
			self.key = key
			return True
		else:
			return False
			
		
		
	def encrypt(self, text):
		ct = ''
		modKey = self.key
		size = len(modKey)
		if(len(text) > len(modKey)):
			for i in range(0,len(text) + 1):
				if(i > size):
					modKey += modKey[i - size - 1]
		for i in range(len(text)):
			ct += chr((((ord(text[i]) + (ord(modKey[i]) - 97)) - 97) % 26) + 97)
		print(ct)
		
			

	def decrypt(self, text):
		pt = ''
		modKey = self.key
		size = len(modKey)
		if(len(text) > len(modKey)):
			for i in range(0,len(text) + 1):
				if(i > size):
					modKey += modKey[i - size - 1]
		for i in range(len(text)):
			pt += chr((((ord(text[i]) - (ord(modKey[i]) - 97)) - 97) % 26) + 97)
		print(pt)
	
