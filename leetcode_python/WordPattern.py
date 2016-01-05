# leetcode WordPattern problem

#arr1 = str.split("dog cat cat dog")

#for i in range(len(arr1)):
#    print(arr1[i])

def WordPattern(pattern, str):
    arr1 = str.split()
    dict1, dict2 = {}, {}
    for k,v in zip(pattern, arr1):
        #print(k+" "+v)
        if k not in dict1:
            dict1[k] = v
        if v not in dict2:
            dict2[v] = k
        if(dict1[k]!=v) or (dict2[v]!=k):
            return False
    return True

print(WordPattern("abba", "dog cat cat dog"))
print(WordPattern("abba", "dog cat cat fish"))
print(WordPattern("aaaa", "dog cat cat dog"))
print(WordPattern("abba", "dog dog dog dog"))


