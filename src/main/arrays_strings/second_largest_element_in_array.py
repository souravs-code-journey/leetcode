class Solution:
    def secondLargestElement(self, nums):

        if len(nums) < 2:
            return -1
        largest = float('-inf')
        second_largest = float('-inf')

        for item in nums:
            if item > largest:
                second_largest = largest
                largest = item
            elif item > second_largest and item != largest:
                second_largest = item

        return second_largest


if __name__ == "__main__":
    nums = [10, 10, 10, 10, 10]
    sol = Solution()
    result = sol.secondLargestElement(nums)
    print(f"second largest is :", result)
