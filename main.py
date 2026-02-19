from enigma import *

rotors = ["", "", "", ""]
offsets = [charToInt("a"), charToInt("a"), charToInt("a")]
plugs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


while len(rotors[0]) == 0:
    ref = input("Reflector A, B, or C: ")
    if ref.lower() == "a" or ref.lower() == "b" or ref.lower() == "c":
        rotors[0] = ref.lower()
    else:
        print(ref + " is not a valid input")

def setrotors():
    ref = input("Rotors. Example \"213\": ")
    if len(ref) == 3:
        if ref.isnumeric():
            for i in range(len(ref)):
                if (ref[i] == "1" or ref[i] == "2" or ref[i] == "3"):
                    rotors[i+1] = ref[i]
                    
                else: 
                    print(ref + " is not a valid input")
                    setrotors()
        else: 
            print(ref + " is not a valid input")
            setrotors()
    else:
        print(ref + " has the wrong length")
        setrotors()

def setoffset():
    ref = input("Offset letters. Example \"AAA\": ")
    if len(ref) == 3:
        if ref.isalpha() :
            for i in range(len(ref)):
                offsets[i] = charToInt(ref[i])
        else: 
            print(ref + " is not a valid input")
            setoffset()
    else:
        print(ref + " has the wrong number of letters")
        setoffset()

def setplugs():
    ref = input("(optional) Plug board settings. Example \"AG TE PO ML\": ")
    if len(ref) > 0:
        arr = ref.split(" ")
        for i in arr:
            if i.isalpha():
                plugs[charToInt(i[0])] = charToInt(i[1])
                plugs[charToInt(i[1])] = charToInt(i[0])
            else: 
                print(ref + " is not a valid input")
                setplugs()    

setrotors()
setoffset()
setplugs()

print(enigma(rotors[0], rotors[1], rotors[2], rotors[3], offsets[0], offsets[1], offsets[2], plugs, input("type your message here: ").lower()))