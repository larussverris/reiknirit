#include<iostream>;
#include<vector>;
#include <math.h>
using namespace std;

/*
int index(vector<int> &vect, int tala){
	for (int i = 0; i < vect.size(); i++){
		if (vect[i] == tala){
			return i;
		}
	}
	return -1;
}
*/

void block_erase(vector<int> &vect, int a, int b){
	for (int i = a; i < b; i++){
		vect.erase(vect.begin() + i);
	}
}

/*
void b_search(vector<int> &vect, int tala){
	int middle = floor(vect.size() / 2);
	if(middle < tala){
		vect.erase(middle+vect.size());
	}
	else if (middle > tala){
		vect.erase(vect.begin() + middle);
	}
	for (int i = 0; i < vect.size(); i++){
		cout << vect[i] << "," << endl;
	}
}
*/



int main(){
	/*
	vector<int> larus = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
	cout << index(larus, 88) << endl;
	*/
	vector<int> larus = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 };
	block_erase(larus, 2, 7);
	for (int i = 0; i < larus.size(); i++){
		cout << larus[i] << endl;
	}
	system("pause");
	return 0;
}