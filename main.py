class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict={}
        for j in range(len(nums)):
            if nums[j] in new_dict:
                return [new_dict[nums[j]],j]
            else:
                newkey=target-nums[j]
                new_dict[newkey]=j 
