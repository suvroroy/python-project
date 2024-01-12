'''
Convert Uppercase Characters To Lowercase
Convert all uppercase characters to lowercase in a given string.

Example One
{
"s": "InTerView"
}
Output:

"interview"
Example Two
{
"s": "KICKSTART"
}
Output:

"kickstart"

'''

def upper_to_lower(s):
    lcs = ''

    for x in s:
        if x.isupper():
            lcs += x.lower()
        else:
            lcs += x
    return lcs

print(upper_to_lower("InTerView"))