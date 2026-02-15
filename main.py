def charToInt(char):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(len(letters)):
        if (char == letters[i]):
            return i
def intToChar(num):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    return letters[num]
        

rotors = [[], [], [], []]
offsets = [charToInt("a"), charToInt("a"), charToInt("a")]

rotor1 = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
rotor2 = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
rotor3 = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]

reflectora = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
reflectorb = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
reflectorc = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

 
while len(rotors[0]) == 0:
    ref = input("Reflector A, B, or C: ")
    if ref.lower() == "a":
        rotors[0] = reflectora
    elif ref.lower() == "b":
        rotors[0] = reflectorb
    elif ref.lower() == "c":
        rotors[0] = reflectorc

while len(rotors[1]) == 0:
    ref = input("Rotor 1, 2, or 3: ")
    if ref.lower() == "1":
        rotors[1] = rotor1
    elif ref.lower() == "2":
        rotors[1] = rotor2
    elif ref.lower() == "3":
        rotors[1] = rotor3
    
while len(rotors[2]) == 0:
    ref = input("Rotor 1, 2, or 3: ")
    if ref.lower() == "1":
        rotors[2] = rotor1
    elif ref.lower() == "2":
        rotors[2] = rotor2
    elif ref.lower() == "3":
        rotors[2] = rotor3

while len(rotors[3]) == 0:
    ref = input("Rotor 1, 2, or 3: ")
    if ref.lower() == "1":
        rotors[3] = rotor1
    elif ref.lower() == "2":
        rotors[3] = rotor2
    elif ref.lower() == "3":
        rotors[3] = rotor3

def setoffset():
    ref = input("Offset letters \"XXX\": ")
    for i in range(len(ref)):
        if ref[i].isalpha:
            offsets[i] = charToInt(ref[i])
        else: 
            print("try again")
            setoffset()

setoffset()


string = input("type your message here: ").lower()
result = ""

for i in string:
    if i == " ":
        result+=" "
    else:
        offsets[2] = (offsets[2] + 1) % 26
        if(offsets[2] == charToInt("w")):
            if(offsets[1] == charToInt("e")):
                offsets[0] = (offsets[0] + 1) % 26
            offsets[1] = (offsets[1] + 1) % 26


        c = (charToInt(i) + offsets[2]) % 26
        c = (rotors[3][c] - offsets[2]) % 26

        c = (c + offsets[1]) % 26
        c = (rotors[2][c] - offsets[1]) % 26

        c = (c + offsets[0]) % 26
        c = (rotors[1][c] - offsets[0]) % 26

        c = rotors[0][c]
        
        c = rotors[1].index((c + offsets[0]) % 26)
        c = (c - offsets[0]) % 26
        
        c = rotors[2].index((c + offsets[1]) % 26)
        c = (c - offsets[1]) % 26
        
        c = rotors[3].index((c + offsets[2]) % 26)
        c = (c - offsets[2]) % 26
        
        result += intToChar(c)



print(result)