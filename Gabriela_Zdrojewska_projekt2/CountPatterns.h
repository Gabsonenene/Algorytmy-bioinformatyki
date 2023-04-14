#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class CountPatterns{
	
	private:
	string sekwencja;//badany lancuch
	fstream oriC_in;//strumien oslugujacy plik
	string czytany_plik;//pamieta nazwe przetwarzanego pliku
	string szukany_pattern;//pamieta poszukiwany wzorzec
	string komp_nic;//komplementarna sekwencje calego lancucha oriC
	vector <int> lokalizacja;//wektor zawierajacy lokalizacje badanej sekwencji
	int count;//ilosc wystapienia danego k-meru; w funkcji (metodzie) count_pattern
	string kompsekw;//sekwencja komplementarna podanego k-meru ("ATGATCAAG")
	vector <int> przefilrowane_lokalizacje;//wektor zawierajacy lokalizacje wystepujace blisko siebie danego k-meru
	
	public:
	~CountPatterns();//destruktor
	CountPatterns(string plik_do_czytania);//konstruktor wywoluje nazwe pliku do czytania danych
	CountPatterns(string plik_do_czytania, int dlugosc);//drugi konstruktor szukajacy w pliku dlugosci najczestszego wzorca
	void czytajPlik(string nazwa_pliku);//laduje podany plik
	void wyswietl_sekwencje();//wydruk zawartosci badanego lancucha
	void stworz_kompl();//metoda pozwalajaca stworzyc komplementarna sekwencjê 
	void wyswietl_kompl();//metoda wyswietlajaca komplementarna sekwencje calego lancucha oriC
	void pattern_count(string);//metoda liczaca ile razy wystapil dany k-mer i jaka jest jego dlugosc, pobiera stringa
	void lokalizacjaa(string);//metoda pozwalajaca znalezc lokalizacje szuaknego k-meru, pobiera stringa
	void wyswietl_pattern_count();//metoda wyswietlajaca wyniki metody pattern_count, czyli badany k-mer, jego dlugosc, ilosc wystapien i lokzalizacje
	void najczestsze_wzorce(int);//metoda sluzaca do odnalezienia najczestszych wzorcow, pobiera int
	void stworz_komplsekw(string pattern);//metoda sluzaca do stworzenia komplementarnej sekwencji dla podanego k-mera ("ATGATCAAG")
	void wyswietl_komplsekw();//metoda wyswietlajaca komplementarna sekwencje dla podanego k-meru
	void lokalizacjaFiltr(int max_roznica);//metoda wyznaczajaca odleglosci pomiedzy badanymi wzorcami
	
};

