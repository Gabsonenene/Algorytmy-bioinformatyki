#include "CountPatterns.h"

//konstruktor nr 1:
CountPatterns::CountPatterns(string nazwa_pliku){
    czytajPlik(nazwa_pliku);
}

//konstruktor nr 2:
CountPatterns::CountPatterns(string nazwa_pliku, int dlugosc){
	czytajPlik(nazwa_pliku);
	najczestsze_wzorce(dlugosc);
}


void CountPatterns::wyswietl_sekwencje(){
	cout << "Zawartosc pliku " << czytany_plik << endl;
	cout << "Sekwencja oriC: \n" << sekwencja << endl;
}


void CountPatterns::czytajPlik(string nazwa_pliku){
	oriC_in.open(nazwa_pliku.c_str());
    if (oriC_in.is_open()) cout << endl << "Analizowany bedzie " << nazwa_pliku << endl;
    else{cout << nazwa_pliku << " jest niedostepny. Koncze \n";
    }
    czytany_plik = nazwa_pliku;
    vector<string> linie;
    string jedna_linia;
    while(!oriC_in.eof()){
        oriC_in >> jedna_linia;
        linie.push_back(jedna_linia);
    }

    for(vector<string>::iterator it = linie.begin(); it != linie.end();++it){
        sekwencja.append(*it);
    }
}


void CountPatterns::stworz_kompl(){
		for (int i=sekwencja.size() - 1; i>=0; i--){
		char znak = sekwencja.at(i);//sprawdzam ka¿dy znak po kolei. Korzystam z char, poniewa¿ dzia³am na pojedyñczych znakach. at - zwraca znak w podanym indeksie.
		if (znak == 'a'){
			komp_nic += 't';
			continue;
		}
		else if (znak == 't'){
			komp_nic += 'a';
			continue;
		}
		else if (znak == 'c'){
			komp_nic += 'g';
			continue;
		}
		else if (znak == 'g'){
			komp_nic += 'c';
			continue;
		}
	}
}


void CountPatterns::wyswietl_kompl(){
	cout << "\nKomplementarna nic: \n" << komp_nic << endl;
	
}


void CountPatterns::pattern_count(string kmer){
	szukany_pattern=kmer;
	count=0;
	for (int i=0; i<sekwencja.size() - kmer.size(); i++){
		if (sekwencja.substr(i,kmer.size()) == kmer){
			count++;
		}
	}
	
}


void CountPatterns::lokalizacjaa(string kmer){
	lokalizacja.clear();
	for (int i=0; i<sekwencja.size() - kmer.size(); i++){
		if (sekwencja.substr(i,kmer.size()) == kmer){
			lokalizacja.push_back(i);
		}
	}
	
}


void CountPatterns::lokalizacjaFiltr(int max_roznica){
	przefilrowane_lokalizacje.clear();
	cout<<"Lokalizacje posiadajace identyczny wzor odlegly o mniej niz "<<max_roznica<<":"<<endl;
	for (vector<int>::iterator ite = lokalizacja.begin()+1; ite!= lokalizacja.end()-1; ++ite){
		
		if (*ite - *(ite-1)<=max_roznica || *(ite+1)-*ite <=max_roznica){
			cout <<"Pozycja "<< *ite<<endl;
			przefilrowane_lokalizacje.push_back(*ite);
		}
		}
}


void CountPatterns::wyswietl_pattern_count(){
	cout << "\nSzukana sekwencja: " << szukany_pattern << endl;
	cout << "Dlugosc szukanej sekwencji: " << szukany_pattern.size() << endl;
	cout << "Ilosc wystapien: " << count << endl;
	cout << "Lokalizacja: \n";
        for (vector<int>::iterator ite = lokalizacja.begin(); ite!= lokalizacja.end(); ++ite){
		cout << *ite << endl;}
}


void CountPatterns::najczestsze_wzorce(int kmer){
	vector <string> frequent_patterns;
	vector <int> ilosc;
	
		if(ilosc.size()){
			ilosc.erase(ilosc.begin(), ilosc.end());
		}
	for(int i=0; i<sekwencja.size()-kmer; i++){
		string pattern = sekwencja.substr(i,kmer);
		pattern_count(pattern);
		ilosc.push_back(count);
	}
	
	//szukamy maksymalne elementy, które wsyt¹pi³y w ,,ilosc"
	int max_count=0;
	for (int i=0; i<ilosc.size(); i++){
		if(ilosc[i]>max_count){
			max_count = ilosc[i];
		}
	}
	
	//Usuniêcie powtarzaj¹cych siê wzorców:
	string bylo="";//elementy, które zosta³y wyœwietlone; na pocz¹tku string bylo jest pusty
	for (int i=0; i<ilosc.size()-kmer; i++){
		if(ilosc[i]==max_count){
			if (bylo.find(sekwencja.substr(i,kmer))==string::npos){
				frequent_patterns.push_back(sekwencja.substr(i,kmer));
				bylo += sekwencja.substr(i,kmer);
			}
		}
		}
		
	//Wyswietlamy wyniki:
	cout<<"rozmiar: "<<kmer<<" krotnosc: "<<max_count<<" mialy slowa: ";
	for (vector<string>::iterator ite=frequent_patterns.begin(); ite!=frequent_patterns.end(); ++ite){
		cout <<*ite<<"\t";
		
}
	cout<<endl;
}
	
	
void CountPatterns::stworz_komplsekw(string pattern){
		for (int i=pattern.size() - 1; i>=0; i--){
		char znak = pattern.at(i);//sprawdzam ka¿dy znak po kolei. Korzystam z char, poniewa¿ dzia³am na pojedyñczych znakach. at - zwraca znak w podanym indeksie.
		if (znak == 'A'){
			kompsekw += 'T';
			continue;
		}
		else if (znak == 'T'){
			kompsekw += 'A';
			continue;
		}
		else if (znak == 'C'){
			kompsekw += 'G';
			continue;
		}
		else if (znak == 'G'){
			kompsekw += 'C';
			continue;
		}
	}
}


void CountPatterns::wyswietl_komplsekw(){
	cout << "\n\nKomplementarna sekwencja do ATGATCAAG to: \n" << kompsekw << endl;
}

//Zapisanie lokalizacji do pliku; sprawdzenie dzialania destruktora; otwiera nam w folderze plik zapis.txt z pozycja/ami, ktore znajduja sie blisko siebie
CountPatterns::~CountPatterns(){
	ofstream myfile;
	myfile.open("zapis.txt");
	for (vector<int>::iterator ite = przefilrowane_lokalizacje.begin(); ite != przefilrowane_lokalizacje.end(); ++ite){
		myfile<< *ite << endl;
		}
	myfile.close();
}
