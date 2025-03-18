class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        filter = [[i,j] for i in range(len(nums)) for j in range(len(nums)) if nums[i]+nums[j] == target and i !=j]
        print(filter)
        return filter[0]



x =  Solution()

x.twoSum([3,3],6)