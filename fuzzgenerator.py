
def fuzzme(fuzzlen):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    fuzzbuff = []
    i = 0
    alphacount = 0
    fourcount = 0
    while i < fuzzlen:
        fuzzbuff.append(alphabet[alphacount])
        fourcount += 1
        if(fourcount == 4):
            fourcount = 0
            if(alphacount == 25):
                alphacount = 0
            else:
                alphacount += 1
        i += 1
    print("".join(fuzzbuff))

fuzzme(12000)