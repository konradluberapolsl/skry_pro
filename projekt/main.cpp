#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void files(string);


int main()
{
	files("chuj");
	system("pause");
}

void files(string name)
{
	fstream plik;
	plik.open("slowa.txt", ios::in);
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