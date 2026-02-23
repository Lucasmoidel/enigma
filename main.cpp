#include <iostream>
#include "enigma.h"
int main(){
    std::cout << enigma("b", "1", "2", "3", 0, 0, 0, (int[]){0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}, "aaaaa") << "\n";
    return 0;
}