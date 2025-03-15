from typing import  List

class Solutions:
    def two_sum_hashing(self, nums:List, target:int):
        """
        1. create a hashset where we can store the element which we have browsed and its index in the nums
        2. calculate the target - nums[i] as we need two numbers to add up to the target
        3. iterate through the nums and check if the target - nums[i] already exists in the hashset
        4. If its already there it means we have found the two numbers and their indexes are the index of the element stored
           in the hashset and the index of the current element we are iterating
        :param nums: List of elemets
        :param target: the target number for which we need to find the index of  two numbers which add up to target.
        :return:
        """
        flag = 0
        hashset= {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in hashset:
                flag = 1
                print( i, hashset[complement] )
            else:
                hashset[nums[i]] = i
        if flag == 0:
            print(f"No two numbers add up to {target}")


if __name__ == '__main__':
    target = 8
    nums = [5,2,7,10,3,9]

    s = Solutions()
    s.two_sum_hashing(nums,target)