class Solution:
    def moveZeroes(self, nums):
        # 思路：双指针方法
        j = 0
        for i in range(len(nums)):
            print('-----')
            print(i)
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                print('****')
                print(j)

nums = [0, 3, 4, 0, 5]
Solution().moveZeroes(nums)

# 思路：遍历列表时，计算0的数量，并剔除0，最后在列表尾部添加同等数量的0
