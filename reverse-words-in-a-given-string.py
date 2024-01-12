'''
Reverse Words In A Given String
Given a string s, your task is to reverse the words of s.

Example One
{
"s": "best technical interview prep courses",
}
Output:

courses prep interview technical best
Example Two
{
"s": "kickstart",
}
Output:

kickstart
'''


def reverse_words_in_string(s):
    l = []
    rl = []
    rs = ''
    l = s.split()
    j = len(l) - 1
    while j >= 0:
        rl.append(l[j])
        j -= 1
    for x in rl:
        rs = rs+' '+x
    mod_rs = rs[1:]
    # rs = str(rl)
    # print("type of rs ", type(rs))
    return mod_rs

# print(reverse_words_in_string("best technical interview prep courses"))
# print(reverse_words_in_string("kickstart"))
print(reverse_words_in_string("best technical"))