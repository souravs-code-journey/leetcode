class Solution:
    def reverseArray(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def rotateArray(self, nums, k):
        n = len(nums)
        k = k % n

        # reverse first k elements
        self.reverseArray(nums, 0, k - 1)

        # reverse the last n-k elements
        self.reverseArray(nums, k, n - 1)

        # reverse the entire array
        self.reverseArray(nums, 0, n - 1)

def printArray(nums):
    for val in nums:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    k = 2

    print("Initial array: ")
    printArray(nums)

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to rotate the array to the left by k places
    sol.rotateArray(nums, k)

    print(f"Array after rotating elements by {k} places: ")
    printArray(nums)
