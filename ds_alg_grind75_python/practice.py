

def isPalindrome(input:str):
    # "A man, a plan, a canal: Panama" --> "amanaplanacanalpanama"
    alphanum_input = "".join([char for char in input if char.isalnum()]).lower()
    print(alphanum_input)

    start, end = 0, len(input) -1

    while start > end:
        if input[start] != input[end]:
            return False
        start += 1
        end -= 1
            
    return True



print(isPalindrome("A man, a plan, a canal: Panama") == True)
print(isPalindrome("race a car") == False)
print(isPalindrome(" ") == True)

