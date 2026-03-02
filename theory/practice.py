# Valid Palindrome

def isPalindrome(input: str):
    
    """
    Solution 1
    alphanum_str=""
    for char in input:
        if char.isalnum():
            alphanum_str += char
    """

    """
    Solution 2
    alphanum_str = "".join(filter(str.isalnum, input))
    """

    """
    Solution 3
    """

    alphanum_str = "".join([char for char in input if char.isalnum()])
    print(alphanum_str.lower())

    start = 0
    end = len(alphanum_str)-1

    while start < end:
        if alphanum_str[start].lower() != alphanum_str[end].lower():
            return False
        start += 1
        end -= 1

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))

# Palindrome Number
def isPalindrome(num):
    #return str(num) == str(num)[::-1]

    if num <= 0 or (num % 10 == 0):
        return False
    
    reversed_num = 0

    while num > reversed_num:
        reversed_num += reversed_num *10 + num % 10
        num = num // 10
    return num == reversed_num or num == reversed_num//10


print(isPalindrome(121))
print(isPalindrome(123454))
print(isPalindrome(10))