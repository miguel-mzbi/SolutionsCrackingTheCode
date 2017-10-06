#include <string>
#include <iostream>

using namespace std;

void reverse(char *str) {
    if(str){
        char * end = str;            
        while(*end != '\0') {
            end++;            
        }
        end--;
        char temp;
        while(end > str) {
            temp = *str;
            *str = *end;
            *end = temp;
            str++;
            end--;
        }
    }
}

int main() {
    string s = " ";
    char * str = new char[s.size()+1];
    copy(s.begin(), s.end(), str);
    str[s.size()] = '\0';
    reverse(str);
    for(int i = 0; i < s.size(); i++) {
        cout << str[i];
    }
    delete[] str;
    
}