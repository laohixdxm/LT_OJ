#leetcode IsAnagram by hashtable 

def IsAnagram(s1, s2):
    dict1, dict2 = {}, {}
    for i in range(len(s1)):
        if(s1[i] not in dict1):
            dict1[s1[i]] = 1
        else:
            dict1[s1[i]] += 1
    for i in range(len(s2)):
        if(s2[i] not in dict2):
            dict2[s2[i]] = 1
        else:
            dict2[s2[i]] += 1
    return dict1==dict2

print(IsAnagram("aab", "aba"))
print(IsAnagram("aab", "abb"))






