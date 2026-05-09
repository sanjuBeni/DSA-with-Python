
# string = "abcdefedcba"
string = "abcdefedcbakjsjhkjg fskd"

# TC : O(n/2) ~ O(n)
# SC : O(n) - Stack Space

def is_palindrome(str, right_idx, left_idx = 0):
    if len(str) == 0:
        return False
    if len(str) == 1:
        return True
    if left_idx >= right_idx:
        return True
    
    if str[left_idx] == str[right_idx]:
        return is_palindrome(str, right_idx-1, left_idx+1)
    else: 
        return False
    
# print(is_palindrome(string, len(string)-1))


def is_pal(str):
    left_idx = 0
    right_idx = len(string) -1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        
        left_idx += 1
        right_idx -= 1
    
    return True

print(is_pal(string))