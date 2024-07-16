def reverseWords(sentence):
    return " ".join(reversed(sentence.split()))

#Example 1:
#Input:
s = "the sky is blue"
print('=='+reverseWords(s)+'==')
#Output: "blue is sky the"

#Example 2:
#Input: 
s = "  hello world  "
print('=='+reverseWords(s)+'==')
#Output: "world hello"
#Explanation: Your reversed string should not contain leading or trailing spaces.

#Example 3:
#Input: 
s = "a good   example"
print('=='+reverseWords(s)+'==')
#Output: "example good a"
#Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
