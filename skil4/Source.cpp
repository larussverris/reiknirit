#include<iostream>
#include<vector>
using namespace std;

// skilaverkefni 4 í reikniritum - Lárus Arnar

// fall sem finnur index af tölu í lista
int index(vector<int> &vect, int tala){
    for (int i = 0; i < vect.size(); i++){ // fallið forloopar í gegn um listann
        if (vect[i] == tala){ return i;} // fallið athugar hvort index-ið jafngildir tölunni og skilar svo index-inu ef það finnst
    } return -1; // annars skilar fallið -1
}

// fall sem finnur index af tölu með binary search algrími
int bSearch(vector<int> &vect, int tala, int b, int a = 0){
    if (a <= b) { // ef low pointer er minni eða jafn high pointer
        int middle=(a+b)/2; // miðjan fundin með þvi að leggja saman hi og lo og deila með 2
        if(tala == vect[middle]){ return middle;} // ef miðgildið jafngildir tölunni sem leitað er eftir þá er hún augljóslega fundin
        if(vect[middle]<tala){a = middle+1;} // ef talan er hærri en miðgildið þá verður low pointerinn að miðgildinu (leita þarf í seinni helmingnum)
        if(vect[middle]>tala){b = middle-1;} // ef talan er minni en miðgildið á verður hi pointerinn að miðgildinu (leita þarf í fyrri helmingnum)
        return bSearch(vect, tala, b, a); // fallið kallar á sjálft sig
    } return -1; // annars skilar fallið -1
}

// fall sem bætir inn tölu á réttan stað í lista
int add(vector<int> &vect, int tala){
    for (int i = (int)(vect.size())-1; i>=0; i--) { // loopar öfugt í gegn um listann
        if (tala >= vect[i]) {  // ef talan er stærri eða jöfn gildinu
            vect.insert(vect.begin() + i+1, tala ); // bætir tölunni inn á réttan stað
            return true;
        }
    }
    vect.insert(vect.begin(),tala); // annars bætir það tölunni fremst í listann
    return true;
}


int main(){
    vector<int> listi = {7, 8, 9, 10, 11, 12, 13, 14, 15};
    vector<int> tolur = {1, 2, 3, 4, 6, 7, 8, 9};

    //cout << index(listi, 10) << endl;                        // index search
    //cout << bSearch(listi, 11,(int)(listi.size())) << endl;  // binary search
        
    /*
    add(tolur,6);   					       // fall sem setur tölu á réttan stað
 
    for(int i=0;i<tolur.size();i++) {                          // lykkja til að prenta "tolur" listann
        cout<<tolur[i]<<", ";
    }
    */
    return 0;
}
