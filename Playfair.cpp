#include "Playfair.h"
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

/**
 * Sets the key to use
 * @param key - the key to use
 * @return - True if the key is valid and False otherwise
 */
bool Playfair::setKey(const string& key,char* table)
{
	string temp = key;
	int j = 0;
	char a[25] = {'A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
	vector<char> alphabet(a, a + sizeof(a) / sizeof(a[0]));
	//erase multiples in key
	for(int i=0; i < key.length(); i++)
	{
	   temp[i] = toupper(temp[i]);
	   if(find(alphabet.begin(), alphabet.end(), key[i]) != alphabet.end())
	   {
		int pos = distance(alphabet.begin(), find(alphabet.begin(), alphabet.end(), key[i]));
	   	alphabet.erase(alphabet.begin() + pos);
	   }
	   else
	   {
		temp.erase(i, i+1);
	   }
	}
	for(int i=0; i < 5; i++)
	{
	   for(int k=0; k < temp.length(); k++)
	   {
	     if(k%5 == 0)
		j++;
	     temp[i] = toupper(temp[i]);
	     table[i][j] = temp[k];
	   }
	}	
	return false;  
}


/**	
 * Encrypts a plaintext string
 * @param plaintext - the plaintext string
 * @return - the encrypted ciphertext string
 */
string Playfair::encrypt(const string& plaintext)
{ 
	
	
	return ""; 
}

/**
 * Decrypts a string of ciphertext
 * @param cipherText - the ciphertext
 * @return - the plaintext
 */
string Playfair::decrypt(const string& cipherText) 
{ 
	return ""; 
	
}

