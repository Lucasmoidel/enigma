#include <iostream>
#include "enigma.h"
int main(){
    std::string reflector;
    std::string rotors;
    std::string offsets;
    std::string text;

    while (reflector.size() < 1){
        std::cout << "Reflector A, B, or C: ";
        std::cin >> reflector;
    }

    while (rotors.size() < 3){
        std::cout << "Rotors. Example \"213\":";
        std::cin >> rotors;
    }

    while (offsets.size() < 3){
        std::cout << "Offset letters. Example \"AAA\":";
        std::cin >> offsets;
    }

    while (text.size() < 1){
        std::cout << "type your message here: ";
        std::cin >> text;
    }

    std::cout << enigma::enigma(
        reflector,
        rotors.substr(0, 1),
        rotors.substr(1, 1),
        rotors.substr(2, 1),
        offsets.substr(0, 1),
        offsets.substr(1, 1),
        offsets.substr(2, 1),
        (int[]){0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25},
        text
    ) << "\n";
    return 0;
}