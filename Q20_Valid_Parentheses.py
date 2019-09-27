s = "){"


def isValid(s):
    if s == "":
        return True
    if len(s) % 2 != 0:
        return False
    brackets_map = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    try:
        result = [brackets_map[s[i]] != s[i + 1] for i in range(0, int(len(s) - 1), 2)]
        if sum(result) == 0:
            return True
        else:
            result = [brackets_map[s[i]] != s[len(s) - 1 - i] for i in range(int(len(s) / 2))]
            if sum(result) == 0:
                return True
    except:
        try:
            result = [brackets_map[s[i]] != s[len(s)-1-i] for i in range(int(len(s) / 2))]
            if sum(result) == 0:
                return True
        except:
            return False
    return False


print(isValid(s))
