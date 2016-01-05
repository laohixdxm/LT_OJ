#leetcode BullsCows

#def getHint(self, secret, guess):
def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    dict1, dict2 = {}, {}
    for i in range(len(secret)):        
        if(secret[i] not in dict1):
            dict1[secret[i]] = 1
        else:
            dict1[secret[i]] += 1
    print(dict1)

    for j in range(len(guess)):            
        if(guess[j] not in dict2):
            dict2[guess[j]] = 1            
        else:
            dict2[guess[j]] += 1
    print(dict2)

    cows = 0
    for i in dict2:
        if(i in dict1):
            cows += min(dict1[i], dict2[i])
    print("cows", cows)

    bulls=0
    for i in range(len(guess)):
        if(guess[i] == secret[i]):
            bulls += 1
            cows -= 1

    #print(bulls, "A", cows, "B")
    res = str(bulls) + "A" + str(cows) + "B" 
    return res

print(getHint("1807", "7810"))
print(getHint("1123", "0111"))
