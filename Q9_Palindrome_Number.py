def isPalindrome(self, x: int) -> bool:
    x = str(x)
    result = [x[num] == x[-num-1] for num in range(int(len(x)/2)+1)]
    if sum(result) == 0:
        return False
    return True
