strs = ["flower","flow","flight"]
test = ["a"]

def longestCommonPrefix(strs):
    result = ""
    if [len(s) for s in strs]:
        least_length = min([len(s) for s in strs])
        for i in range(least_length):
            letter = set([word[i] for word in strs])
            if len(letter) == 1:
                result += list(letter)[0]
            else:
                return result
    return result


print(longestCommonPrefix(test))
