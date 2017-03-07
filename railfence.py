#!/usr/bin/python3


class Rail:

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
		extras = len(text) % self.key
		if(extras >= 1):
			railLen = (len(text)/ self.key) + 1
		else:
			railLen = (len(text)/ self.key)
		matrix = [[0 for x in range(railLen)] for y in range(self.key)] 
		#meetme
		print(len(text))
		for i in range(len(text)):
			for j in range(self.key):
				matrix[j][i] = text[i]
				print(matrix[0])
				print(matrix[1])
		print(matrix[0])

	def decrypt(self, text):
		pt = ''
		for i in range(len(text)):
			pt += chr((((ord(text[i]) - (self.key%26)) - 97) % 26) + 97)
		print(pt)
	
