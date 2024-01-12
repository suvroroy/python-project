'''
Given a list of integers numbers, calculate the pivot index of this list.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the
sum of all the numbers strictly to the index's right. If the index is on the left edge of the array,
 then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example One
{
"numbers": [2, 3, 1, -1, 1, 1, 4]
}
Output:

2
Considering index 2 as pivot index, left subarray = [2, 3] and right subarray = [-1, 1, 1, 4]. Here, sum(left subarray) = sum(right subarray) = 5.

Here, index 4 is also a valid pivot index. But index 2 is leftmost.

Example Two
{
"numbers": [2, 3, 5]
}
Output:

-1
Example Three
{
"numbers": [0, 1, -1]
}
Output:

0
Notes
Constraints:

1 <= size of the input list <= 104
-105 <= any element of the input list <= 105
'''

def left_hand_sum(l,n):
    i = 0
    lhs = 0
    while i<n:
        lhs = lhs + l[i]
        i+=1
    return lhs

def right_hand_sum(l,n):
    rhs = 0
    j = len(l) - 1
    while j > n:
        rhs = rhs + l[j]
        j-=1
    return rhs
def pivot_index(numbers):
    k = 0
    while k < len(numbers):
        if left_hand_sum(numbers, k) == right_hand_sum(numbers, k):
            break
        else:
            k+=1
    if k >= len(numbers):
        k = -1
    return k

print ("pivot index is:", pivot_index([0, 1, -1]))