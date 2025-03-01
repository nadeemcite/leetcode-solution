class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = n-1
            checked = set()
            while l<r:
                if nums[l] + nums[r] == - nums[i]:
                    if nums[l] in checked:
                        l += 1
                    elif nums[r] in checked:
                        r -= 1
                    else:
                        triplets.append([nums[i], nums[l], nums[r]])
                        checked.add(nums[l])
                        checked.add(nums[r])
                        r -= 1
                        l += 1
                elif nums[l] + nums[r] > - nums[i]:
                    r -= 1
                else:
                    l += 1
        return triplets
    

print(Solution().threeSum([0,0,0,0]))
print(Solution().threeSum([-2,0,0,2,2]))
            