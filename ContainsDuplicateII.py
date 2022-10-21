# https://leetcode.com/problems/contains-duplicate-ii/

def containsNearbyDuplicate(nums, k):
    num_dict = {} # dictionary for value -> index mapping
    for i, num in enumerate(nums):
        # if number is present in dictionary, get its index and check if the difference between indices is <= k
        if num in num_dict and i - num_dict[nums[i]] <= k:
            # if yes, return True
            return True
        else:
            # if the number is not present or the number is more than k distance away, update the dictionary with the latest index
            num_dict[num] = i
    return False


# driver code
if __name__ == '__main__':
    nums = [1,2,3,1,2,3]
    k = 1
    print(containsNearbyDuplicate(nums, k))