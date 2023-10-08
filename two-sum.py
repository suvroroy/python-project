def twoSum(nums, target):
    j = 0
    x = 0
    n = len(nums)
    output_indices = []
    while j < (n-1):
        x = j +1
        #print("outer loop...", "j = ", j, "x = ", x)
        while x <= (n -1):
            if ( nums[j] + nums[x] ) == target:
                output_indices = [j, x]
                break
            else:
                x+=1
        j+=1
    return output_indices

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = 0
        x = 0
        n = len(nums)
        output_indices =[]

        while j < (n-1):
            x = j +1
            while x <= (n -1):
                if ( nums[j] + nums[x] ) == target:
                    output_indices = [j, x]
                    break
                else:
                    x+=1
            j+=1

        return output_indices

# print (twoSum([2,7,11,15], 13))
# print (twoSum([3,2,4], 6))
# print (twoSum([3,3], 6))
#print (twoSum([1, 99, 56, 789, 34, 6, 78, 12, 34, 78, 54, 200], 90))
#print (twoSum([3,2,3], 6))
