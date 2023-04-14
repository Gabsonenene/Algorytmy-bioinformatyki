#include <iostream>
#include "CountPatterns.h"

using namespace std;

int main(int argc, char** argv) {
	
	//Testy na oriC
	cout <<"Witaj w obiektowej wersji programu wyszukiwania sekwencji oriC" << endl;
	
	string poszukiwany_plik("oriC.txt");
	string poszukiwany_pattern("atgatcaag");
	
	CountPatterns oric(poszukiwany_plik);
	oric.wyswietl_sekwencje();
	oric.stworz_kompl();
	oric.wyswietl_kompl();
	oric.pattern_count(poszukiwany_pattern);
	oric.lokalizacjaa(poszukiwany_pattern);
	oric.wyswietl_pattern_count();
	oric.lokalizacjaFiltr(600);
	cout << "\n\nNajczestsze wzorce:\n";
	for (int i=3; i<14; i++){
		oric.najczestsze_wzorce(i);
	}
	
	
	cout << "\n\n****************" << endl;
	
	
	//Dla ca�ego genomu cholery; analiza lokalizacji najcz�stszych wzor�w w celu odnalezienia oriC
	poszukiwany_plik = "V_C.fna";
	CountPatterns genom_cholery(poszukiwany_plik);
	poszukiwany_pattern = "ATGATCAAG";
	genom_cholery.pattern_count(poszukiwany_pattern);
	genom_cholery.lokalizacjaa(poszukiwany_pattern);
	genom_cholery.wyswietl_pattern_count();
	genom_cholery.lokalizacjaFiltr(600);
	
	
	poszukiwany_pattern = "CTCTTGATC";
	genom_cholery.pattern_count(poszukiwany_pattern);
	genom_cholery.lokalizacjaa(poszukiwany_pattern);
	genom_cholery.wyswietl_pattern_count();
	genom_cholery.lokalizacjaFiltr(600);
	
	
	poszukiwany_pattern = "TCTTGATCA";
	genom_cholery.pattern_count(poszukiwany_pattern);
	genom_cholery.lokalizacjaa(poszukiwany_pattern);
	genom_cholery.wyswietl_pattern_count();
	genom_cholery.lokalizacjaFiltr(600);

	
	poszukiwany_pattern = "CTTGATCAT";
	genom_cholery.pattern_count(poszukiwany_pattern);
	genom_cholery.lokalizacjaa(poszukiwany_pattern);
	genom_cholery.wyswietl_pattern_count();
	genom_cholery.lokalizacjaFiltr(600);
	
	//komplementarna sekwencja do ATGATCAAG:
	string pattern("ATGATCAAG");
	genom_cholery.stworz_komplsekw(pattern);
	genom_cholery.wyswietl_komplsekw();
	
	
  return 0;
}


//Wnioski:
//Uda�o mi si� odtworzy� tabelk� z podrecznika dla najcz�stszych wzorc�w.
//Sprawdzi�am lokazlizacj� dla czterech 9-mer�w. 9-mer 'ATGATCAAG' w ca�ym genomie wyst�pi� 37 razy.
//Jego lokalizacja, powtarzaj�ca si� trzy razy najcz�ciej w najmniejszych odst�pach od siebie, to:
//2961525
//2961582
//2961653
//Komplementarn� do niego sekwencj� okaza� si� 9-mer 'CTTGATCAT', kt�ry wyst�pi� w ca�ym genomie a� 49 razy.
//Jego lokalizacja w badanym miejscu jest bardzo podobna do lokazlizacji 'ATGATCAAG':
//2961542
//2961923
//2962023
//Pozosta�e dwa 9-mery nie posiadaj� sekwencji, kt�re le�a�yby tak blisko siebie.
//Z tego mo�emy wynioskowa�, �e poszukiwany oriC znajduje si� w lokazliacji od 2961525 do 2962023.

