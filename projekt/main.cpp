#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void files(string);
string encrypt(string);


int main()
{
	files();
	system("pause");
}

void files()
{
	fstream plik;
	plik.open("input/slowa.txt", ios::in);
	if (plik.good())
	{
		string napis;
		cout << "Zawartosc pliku:" << endl;
		while (!plik.eof())
		{
			getline(plik, napis);
			cout << napis << endl;
		}
		plik.close();
	}
	else cout << "Error! Nie udalo otworzyc sie pliku!" << endl;

}

string encrypt(string word)
{

}