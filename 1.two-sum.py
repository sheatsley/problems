#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (45.36%)
# Total Accepted:    2.9M
# Total Submissions: 6.3M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        This implementation is an O(n) solution for twoSum using hash tables.
        The naive brute-force solution (ie two loops, with i < j < n, and
        computing i + j) has an O(n^2) solution. As a general rule of thumb:
        most seemingly simple problems that can be solved in linear time oft do
        so with hash tables (and perhaps some additional datastructure glue).

        For twoSum, the insight stems from the following: Given an initial
        number i and target number t, t - i tells me which number j I need to
        have i + j = t. Seemingly obvious, the subtle part is determining
        whether or not a candidate number is indeed the j we are looking for
        *in constant time.* Enter hash tables.
        
        To know if a candidate number is indeed the j we are looking for, we
        can check for its existence in a hash table. If j exists, then we know
        we have already seen some i such that i + j = t. This is the intuition
        to draw from twoSum. 
        
        As a final note, the requirement of returning the indices for i and j
        is what binds us to a hash table; if instead we were asked to determine
        whether *there exists* some i and j such that i + j = t (ie, a boolean
        question), then a set would be sufficient.
        """
        hashTable = {}
        for i, n in enumerate(nums):
            if n in hashTable:
                return [hashTable[n], i]
            else:
                hashTable[target - n] = i


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
