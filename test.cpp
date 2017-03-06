#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

void setKey(string key,char table[5][5]);

int main()
{
   char a[5][5];
   setKey("Test", a);
   return 0;
}
void setKey(string key,char table[5][5])
{
	string temp = key;
	int j = 0;
	char a[25] = {'A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
	vector<char> alphabet(a, a + sizeof(a) / sizeof(a[0]));
	//erase multiples in key
	for(int i=0; i < temp.length(); i++)
	{
	   temp[i] = toupper(temp[i]);
	   cout << temp[i];
	   if(find(alphabet.begin(), alphabet.end(), key[i]) != alphabet.end())
	   {
		int pos = distance(alphabet.begin(), find(alphabet.begin(), alphabet.end(), key[i]));
	   	alphabet.erase(alphabet.begin() + pos);
	   }
	   else if(i == key.length())
	   {
		temp = temp.substr(0,temp.size()-1);
	   }
	   else
	   {
		temp.erase(i);
	   }
	}
	for(int i=0; i < 5; i++)
	{
	   for(int k=0; k < temp.length(); k++)
	   {
	     if(k%5 == 0)
		j++;
	     temp[k] = toupper(temp[k]);
	     table[i][j] = temp[k];
	   }
	}
 	for(int i=0; i < 5; i++)
	{
	   for(int k=0; k < 5; k++)
	   {
	     cout << table[i][k] << ' ';
	   }
	   cout << '\n';
	}
}
