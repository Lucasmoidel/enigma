def charToInt(char):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(len(letters)):
        if (char == letters[i]):
            return i
def intToChar(num):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    return letters[num]
        

rotor1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 26, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
rotor2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 26, 13, 15, 24, 5, 21, 14, 4]
rotor3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 26, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]

reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 26, 2, 22, 21, 9, 0, 19]

rotor1offset = charToInt("a")
rotor2offset = charToInt("e")
rotor3offset = charToInt("v")


string = input("type your message here: ").lower()
result = ""
for i in string:
    if i == " ":
        result+=" "
    else:
        rotor3offset = (rotor3offset + 1) % 26
        if(rotor3offset == charToInt("w")):
            rotor2offset = (rotor2offset + 1) % 26
        if(rotor2offset == charToInt("f")):
            rotor1offset = (rotor1offset + 1) % 26
        c = (charToInt(i) + rotor3offset) % 26
        c = (rotor3[c] - rotor3offset) % 26

        c = (c + rotor2offset) % 26
        c = (rotor2[c] - rotor2offset) % 26

        c = (c + rotor1offset) % 26
        c = (rotor1[c] - rotor1offset) % 26

        c = reflector[c]
        
        c = rotor1.index((c + rotor1offset) % 26)
        c = (c - rotor1offset) % 26
        
        c = rotor2.index((c + rotor2offset) % 26)
        c = (c - rotor2offset) % 26
        
        c = rotor3.index((c + rotor3offset) % 26)
        c = (c - rotor3offset) % 26
        
        result += intToChar(c)



print(result)