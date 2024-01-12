'''
First Occurrence Of A Character
Find the first occurrence of a given character in a given string.

Example One
{
"s": "interview",
"to_find": "e"
}
Output:

3
Example Two
{
"s": "kickstart",
"to_find": "n"
}
Output:

-1
'''

def first_occurrence_char(s,to_find):
    n = -1
    n = s.find(to_find)
    return n
print(first_occurrence_char('kickstart', 'n'))