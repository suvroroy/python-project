'''
Insert An Element At A Specific Position In An Array
Given an array of numbers, insert a given element at the specified position in the array.

Example One
{
"nums": [2, 4, 5, 6, -1],
"element": 3,
"position": 2
}
Output:

[2, 3, 4, 5, 6]
Example Two
{
"nums": [70, 60, 50, -1],
"element": 40,
"position": 4
}
Output:

[70, 60, 50, 40]
Notes
The last element of the array is -1 indicating a blank position.
The given position follows 1-based indexing.
Return the modified array.
Constraints:

2 <= size of the input array <= 106
0 <= elements of the array <= 106
1 <= position <= size of the input array
'''

def insert_element_in_array(nums, element, position):
    index = position -1
    chop = len(nums)
    nums.insert(index, element)
    modified_nums = nums[0:chop]

    return modified_nums

print ("[70, 60, 50, -1]", insert_element_in_array([70, 60, 50, -1], 40, 4))