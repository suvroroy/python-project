'''
Count Alphabets
Count the number of alphabets in a given string.

Example One
{
"s": "#aBdj12C"
}
Output:

5
Example Two
{
"s": "123 !@#$"
}
Output:

0
'''

def count_nunber_alpha(s):
    # is_alpha = False
    i = 0
    for x in s:
        if x.isalpha():
            i += 1
    return i

print(count_nunber_alpha("123 !@#$"))