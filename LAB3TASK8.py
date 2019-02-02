def is_anagrams(str1,str2):
    str1.lower()
    str2.lower()
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

x = input("Enter First Word to check anagram:")
y = input("Enter Second Word to check anagram:")
print("Is Anagrams:",is_anagrams(x,y))

