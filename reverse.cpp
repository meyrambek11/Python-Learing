#include <iostream>
using namespace std;

int main(){
    string s = "Hello";
    string res = "";
    int j=0;
    for(int i = s.length()-1;i>=0;i--){
        res[j] = s[i];
        cout << res[j];
        j++;
    }
    //cout << res;



}