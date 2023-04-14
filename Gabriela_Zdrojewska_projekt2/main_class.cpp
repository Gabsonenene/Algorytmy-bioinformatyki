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
	
	
	//Dla ca³ego genomu cholery; analiza lokalizacji najczêstszych wzorów w celu odnalezienia oriC
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
//Uda³o mi siê odtworzyæ tabelkê z podrecznika dla najczêstszych wzorców.
//Sprawdzi³am lokazlizacjê dla czterech 9-merów. 9-mer 'ATGATCAAG' w ca³ym genomie wyst¹pi³ 37 razy.
//Jego lokalizacja, powtarzaj¹ca siê trzy razy najczêœciej w najmniejszych odstêpach od siebie, to:
//2961525
//2961582
//2961653
//Komplementarn¹ do niego sekwencj¹ okaza³ siê 9-mer 'CTTGATCAT', który wyst¹pi³ w ca³ym genomie a¿ 49 razy.
//Jego lokalizacja w badanym miejscu jest bardzo podobna do lokazlizacji 'ATGATCAAG':
//2961542
//2961923
//2962023
//Pozosta³e dwa 9-mery nie posiadaj¹ sekwencji, które le¿a³yby tak blisko siebie.
//Z tego mo¿emy wynioskowaæ, ¿e poszukiwany oriC znajduje siê w lokazliacji od 2961525 do 2962023.

