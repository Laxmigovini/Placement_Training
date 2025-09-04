s="abbd"
def longestpalindrome(s):
    def ispalindrome(sub):
        return sub == sub[::-1]
    longest = ""
    n = len(s)
    for i in range(n):
        for j in range(i,n):
            if j-i+1 <= len(longest):
                continue
            substring = s[i:j+1]
            if ispalindrome(substring):
                longest = substring
    return longest
print(longestpalindrome(s))
