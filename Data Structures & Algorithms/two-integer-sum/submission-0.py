class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {

        }

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mydict:
                return[mydict[complement], i]
            mydict[nums[i]]= i
        
#nums = [3, 4, 5] target = 7
#i = 0, complement = 7-3 = 4
#my dict empty, so move to next index and add value at current index to mydict at location of current index