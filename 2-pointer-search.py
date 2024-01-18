'''
Segregate Even And Odd Numbers
Given an array of numbers, rearrange them in-place so that even numbers appear before odd ones.

Example
{
"numbers": [1, 2, 3, 4] --> [4,2,3,1]
}
Output:

[4, 2, 3, 1]

[10, 20, 67, 8, 5, 11, 2, 5, 127]
The order within the group of even numbers does not matter; same with odd numbers. So the following are also correct outputs: [4, 2, 1, 3], [2, 4, 1, 3], [2, 4, 3, 1].
'''

# def segregrate_even_odd ( numbers: list) -> list:
#     left_p = 0
#     right_p = len(numbers) -1
#
#     while right_p > left_p:
#         if numbers[right_p] % 2 == 0:
#             temp = numbers[right_p]
#             numbers[right_p] = numbers[left_p]
#             numbers[left_p] = temp
#             left_p += 1
#         else:
#             right_p-= 1
#
#     return numbers
#
# print(segregrate_even_odd([10, 20, 67, 8, 5, 11, 2, 5, 127]))
#---

def segregrate_even_odd ( numbers: list) -> list:
    left_p = 0
    right_p = len(numbers) -1

    while left_p < right_p:
        if numbers[left_p] % 2 == 0:
            left_p += 1
        else:
            temp = numbers[left_p]
            numbers[left_p] = numbers[right_p]
            numbers[right_p] = temp
            right_p -= 1
    return numbers

print(segregrate_even_odd([1, 2, 3, 4]))