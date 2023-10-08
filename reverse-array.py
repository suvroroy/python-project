'''
Reverse a given list of numbers.

Example One
{
"nums": [50, 35, 78, 66, 17]
}
Output:

[17, 66, 78, 35, 50]
Example Two
{
"nums": [50, 40, 30, 20]
}
Output:

[20, 30, 40, 50]
'''

def reverse_list(numbers):
    numbers.reverse()
    return numbers

print ("reverse of [50, 35, 78, 66, 17] is", reverse_list([50, 35, 78, 66, 17]))