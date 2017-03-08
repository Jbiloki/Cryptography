#!/usr/bin/python3
import math

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
		keyHold = self.key
		iterations = 0
		while(keyHold > iterations):
			for i in range(iterations,len(text),keyHold):
				ct += text[i]
			iterations += 1
		print(ct)
		#meetmeafterthetogaparty
		#mematrhtgpryetefeteoaat
		#0 12 

	def decrypt(self, text):
		pt = ''
		ct = ''
		keyHold = self.key
		skip = int(len(text) % self.key)
		print(skip)
		iterations = 0
		if(int(len(text)) % 2 == 0):
			stepOver = int(len(text)/keyHold) + 1
			print(stepOver)
			#mod gives issue
			for i in range(0,int(len(text)/self.key)):
				for j in range(0,self.key):
					print(pt)
					if(j <= skip):
						pt += text[(stepOver*j) + i]
					else:
						pt += text[(stepOver*j) + i - 1]
			for i in range(0, skip):
				pt += text[(stepOver*skip) + i -1]
				
		else:
			stepOver = int(len(text)/keyHold) + 1
			for i in range(0,int(len(text)/self.key) + 1):
				for j in range(0,self.key):
					if(int(len(text)/2) == i):
						pt += text[i]
					else:
						if(j <= skip):
							pt += text[(stepOver*j) + i]
						else:
							pt += text[(stepOver*j) + i - 1]
			for i in range(0, skip):
				pt += text[(stepOver*skip) + i -1]
				
		print(pt)
	
