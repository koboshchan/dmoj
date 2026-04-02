#include <iostream>
using namespace std;
int main(){
    int month, day;
    cin >> month;
    cin >> day;
    if (month == 2 && day == 18){
        cout << "Special" << endl;
        return 0;
    } else if (month < 2){
        cout << "Before" << endl;
        return 0;
    } else if (month == 2 && day < 18){
        cout << "Before" << endl;
        return 0;
    } else if (month > 2){
        cout << "After" << endl;
        return 0;
    } else if (month == 2 && day > 18){
        cout << "After" << endl;
        return 0;
    }
    return 0;
};