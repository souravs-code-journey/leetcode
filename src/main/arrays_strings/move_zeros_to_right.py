class Solution:
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums


if __name__ == '__main__':
    nums = [0,1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    sol = Solution()
    output = sol.moveZeroes(nums)
    print(output)
