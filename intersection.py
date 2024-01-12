'''Given two lists of numbers, find their intersection.

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
Output:

[]
Notes
The order of elements in the output list does not matter.
The frequency of any number in the intersection must be equal to the minimum of the frequency of that number in both the given lists.
Constraints:

1 <= size of the input lists <= 105
-106 <= any element of the input lists <= 106
'''

# def intersection_two_list(l1, l2):
#     # set1 = set(l1)
#     # set2 = set(l2)
#     # set3 = set.intersection(set1, set2)
#     # output_list = list(set3)
#     output_list = list(set(l1.intersection(l2)))
#     return output_list

def intersection_two_list(l1, l2):
    l3 = []
    i = 0
    for x in l1:
        if x == l2[i]:
            l3.append(x)
        else:
            i+=1

    return l3


print ("intersection value = ", intersection_two_list([4, 2, 2, 3, 1],[2, 2, 2, 3, 3]))