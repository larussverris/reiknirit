//
//  main.cpp
//  skil2-algrim
//
//  Created by Lárus A. on 26/01/2019.
//  Copyright © 2019 Lárus A. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;


int summa(int n, int sum = 0) {
	if (n == 0){
		return sum;
	}
	else {
		sum += n*n;
		return summa(n - 1, sum);
	}
}


void runa(int n, int sum = 0, int yo = 0){
	if (n > 0){
		sum++;
		yo += sum;
		cout << yo << endl;
		runa(n - 1, sum, yo);
	}
}

int thversumma(int n){
	if (n == 0){
		return 0;
	}
	else{
		return (n % 10 + thversumma(n / 10));
	}
}


int samnefnari(int a, int b){
	if (a < b){
		samnefnari(b, a);
	}
	int c = a%b;
	if (c == 0) {
		return b;
	}
	else {
		return samnefnari(b, c);
	}
}


int main() {

	//cout << summa(5) << endl;

	//runa(5);

	//cout << thversumma(12) << endl;

	//cout << samnefnari(270, 192) << endl;
	system("pause");


	return 0;
}
