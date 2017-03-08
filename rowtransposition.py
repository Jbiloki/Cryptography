#!/usr/bin/python3
import math

class Rows:

	def __init__(self):
		self.key = None
		return

	def setKey(self, key):
		try:
			#self.key = int(key)
			return True
		except:
			print("Key is not able to convert to int")
			return False
			
		
		
	def encrypt(self, text):
		ct = ''
		stringKey = str(self.key)
		keyLen = len(str(self.key))
		rowSize = int(len(text)/keyLen)
		textLen = len(text)
		matrix = [[0 for x in range(keyLen)] for y in range(rowSize)]
		print(rowSize)
		for i in range(0,textLen):
			for j in range(keyLen):
				if((j + (i * keyLen)) >= textLen):
					break
				matrix[i][j] = text[j + (i * keyLen)]
		print(matrix)
		for i in range(keyLen):
			for j in range(rowSize):
				print(ct)
				ct += matrix[int(stringKey[i])][j]
				

		print(matrix)
	def decrypt(self, text):
		pt = ''
		
	
