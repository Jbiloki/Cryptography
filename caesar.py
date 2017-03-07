#!/usr/bin/python3

class Caesar:

	def __init__(self):
		self.key = None
		return

	def setKey(self, key):
		try:
			self.key = int(key)
			return True
		except:
			print("Key is not able to convert to int")
			return False
			
		
		
	def encrypt(self, text):
		ct = ''
		for i in range(len(text)):
			ct += chr((((ord(text[i]) + self.key) - 97) % 26) + 97)
		print(ct)

	def decrypt(self, text):
		pt = ''
		for i in range(len(text)):
			pt += chr((((ord(text[i]) - (self.key%26)) - 97) % 26) + 97)
		print(pt)
	
