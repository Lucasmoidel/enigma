def charToInt(char):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(len(letters)):
        if (char.lower() == letters[i]):
            return i
def intToChar(num):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    return letters[num]
        
def enigma(reflector, r1, r2, r3, offset1, offset2, offset3, plugs, message):

    rotors = [[], [], [], []]
    offsets = [charToInt("a"), charToInt("a"), charToInt("a")]
    notch = []

    rotor1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    rotor2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
    rotor3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]

    reflectora = [4, 9, 12, 25, 0, 11, 24, 23, 21, 1, 22, 5, 2, 17, 16, 20, 14, 13, 19, 18, 15, 8, 10, 7, 6, 3]
    reflectorb = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
    reflectorc = [5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 1, 13, 12, 7, 11]

    

    if reflector.lower() == "a":
        rotors[0] = reflectora
    elif reflector.lower() == "b":
        rotors[0] = reflectorb
    elif reflector.lower() == "c":
        rotors[0] = reflectorc


    if r1.lower() == "1":
        rotors[1] = rotor1
        notch.append(charToInt("r"))
    elif r1.lower() == "2":
        rotors[1] = rotor2        
        notch.append(charToInt("f"))
    elif r1.lower() == "3":
        rotors[1] = rotor3
        notch.append(charToInt("w"))
        

    if r2.lower() == "1":
        rotors[2] = rotor1
        notch.append(charToInt("r"))
    elif r2.lower() == "2":
        rotors[2] = rotor2
        notch.append(charToInt("f"))
    elif r2.lower() == "3":
        rotors[2] = rotor3
        notch.append(charToInt("w"))


    if r3.lower() == "1":
        rotors[3] = rotor1
        notch.append(charToInt("r"))
    elif r3.lower() == "2":
        rotors[3] = rotor2
        notch.append(charToInt("f"))
    elif r3.lower() == "3":
        rotors[3] = rotor3
        notch.append(charToInt("w"))



    offsets[0] = offset1
    offsets[1] = offset2
    offsets[2] = offset3

    result = ""

    for i in message:
        if i == " ":
            result+=" "
        else:
            offsets[2] = (offsets[2] + 1) % 26
            if(offsets[1] == notch[1]-1):
                offsets[0] = (offsets[0] + 1) % 26
                offsets[1] = (offsets[1] + 1) % 26
            if(offsets[2] == notch[2]):
                offsets[1] = (offsets[1] + 1) % 26


            c = plugs[charToInt(i)]
            c = (c + offsets[2]) % 26
            c = (rotors[3][c] - offsets[2]) % 26

            c = (c + offsets[1]) % 26
            c = (rotors[2][c] - offsets[1]) % 26

            c = (c + offsets[0]) % 26
            c = (rotors[1][c] - offsets[0]) % 26

            c = rotors[0][c]

            c = rotors[1].index((c + offsets[0]) % 26)
            print(c)

            c = (c - offsets[0]) % 26

            c = rotors[2].index((c + offsets[1]) % 26)
            c = (c - offsets[1]) % 26
            
            c = rotors[3].index((c + offsets[2]) % 26)
            c = (c - offsets[2]) % 26
            
            c = plugs.index(c)

            result += intToChar(c)
    return result