class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def check_twoSum(self):
        left = 0
        right = len(self.nums) - 1

        while left < right:
            curr = self.nums[left] + self.nums[right]
            if curr == self.target:
                return True
            elif curr > self.target:
                right -= 1
            else:
                left += 1
        return False


if __name__ == '__main__':
    nums = [1, 2, 4, 6, 8, 9, 14, 15]
    target = 13
    two_sm = TwoSum(nums, target)
    if two_sm.check_twoSum():
        print(f"{target} achieved")
    else:
        print(f"{target} sum not found")
