'''
Given two lists of numbers, find their intersection.

Example One
{
"a": [4, 2, 2, 3, 1],
"b": [2, 2, 2, 3, 3]
}
Output:

[2, 2, 3]
Example Two
{
"a": [6, 2, 4],
"b": [1, 5, 3, 7]
}

{
"a": [7, 7, 14, 92, 14, 92, 92],
"b": [0, 0, 92, 92, 7]
}

{
"a": [2, 2, 1, 3, 2],
"b": [1, 100, 2, 2, 20, 99, 100]
}
'''


# def intersection_lists(l1, l2):
#     l3 = []
#
#     for x in l1:
#         i = 0
#         while i < len(l2):
#             if x == l2[i]:
#                 l3.append(x)
#                 break
#             else:
#                 i += 1
#     return l3


# print(intersection_lists([4, 2, 2, 3, 1], [2, 2, 2, 3, 3]))
# print(intersection_lists([2, 2, 3], [1, 4, 2, 2, 3, 7]))
def get_intersection_with_maintained_frequency(a, b):
    l3 = []
    for x in a:
        i = 0
        while i < len(b):
            if x == b[i]:
                l3.append(x)
                break
            else:
                i += 1
    return l3

print(get_intersection_with_maintained_frequency([2, 2, 3], [1, 4, 2, 2, 3, 7]))