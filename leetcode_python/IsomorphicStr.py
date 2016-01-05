#leetcode IsoMorphic String

def IsoMorphic(s1, s2):
    dict1, dict2 = {}, {}
    for k,v in zip(s1,s2):
        if(k not in dict1):
            dict1[k] = v
        if(v not in dict2):
            dict2[v] = k
        if(dict1[k] != v) or (dict2[v] != k):
            return False
    return True

print(IsoMorphic("egg", "add"))
print(IsoMorphic("foo", "bar"))
print(IsoMorphic("paper", "title"))












