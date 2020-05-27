#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (55.52%)
# Likes:    780
# Dislikes: 696
# Total Accepted:    532.3K
# Total Submissions: 958.6K
# Testcase Example:  '[1,2,3,1]'
#
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
#
# Example 1:
#
#
# Input: [1,2,3,1]
# Output: true
#
# Example 2:
#
#
# Input: [1,2,3,4]
# Output: false
#
# Example 3:
#
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        This implementation is an O(n) solution for containsDuplicate using a
        set.  Like twoSum, the naive brute-force solution (ie two loops, with i
        < j < len(nums), and computing  if nums[i] == nums[j]) has an O(n^2)
        solution. 

        For containsDuplicate, the insight stems from the following: given some
        numbers i and a new number j, we need to know if j is in i **in constant
        time**. Importantly, in the solution below, if "elements" were a list
        (instead of a set), then our runtime is still O(n^2), as searching 
        through a list is O(n). However, the underlying mechanism for sets 
        (which are ostensibly hash tables without values) is hashing, meaning 
        we can perform a membership test in constant time.

        As a final note, because hash functions are the underlying mechanism
        for sets, sets only contain unique values. Therefore, another one-liner
        solution to this problem is to check if the length of a list is equal
        to the cardinality of the set, ie:

                        return len(nums) == len(set(nums))

        The above approach is asymptotically identical upper-bound to the
        solution below, ie O(n). However, this clever one-liner requires that
        the entire list be iterated over and constructed into a set.  This
        means that the best case for this approach is still bounded by n (ie
        Ω(n)). However, our solution below, in the best case, can be bounded by
        Ω(1) because we can terminate early before iterating through nums
        fully. 
        """
        elements = set([])
        for n in nums:
            if n in elements:
                return True
            else:
                elements.add(n)
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1])
    assert not s.containsDuplicate([1, 2, 3, 4])
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

# @lc code=end
