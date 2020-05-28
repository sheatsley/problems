#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (46.72%)
# Likes:    3972
# Dislikes: 128
# Total Accepted:    647.2K
# Total Submissions: 1.4M
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        This implementation is an O(n) solution for climbStairs using dynamic
        programming. The naive brute-force solution (ie summming two recrusive
        calls with n - 1 and n - 2) has a O(2^n) solution (and will actually
        fail leetcode submissions with a "time limit exceeded" message). A
        one-liner brute-force recursive solution may look like:

            return (1 if n == 0  else 0 if n < 0 else
                        self.climbStairs(n - 2) + self.climbStairs(n - 1))

        This recursive solution has a horrendous exponential runtime and can
        be visualized through the following recursive tree for n == 4:

                                       4
                                    /     \
                               --> 3       2 <--
                                 /   \    / \
                                2     1  1   0
                               / \   /  /
                              1   0 0  0
                             /
                            0

        Notably, we see that we (redundantly) compute n == 2 twice, n == 1
        three times, and n == 0 (our solution nodes) five times. For larger
        values of n, this redundant computation is only exacerbated. This
        observation leads us to a simple question (that will eventually
        lead us to the central insight for climbStairs): how do we remove
        this redundant computation?

        For starters, on the left side of the tree, we can see that node 3
        (with the "-->" arrow) has children 2 and 1. On the right side of the
        tree we can see one of 3's children (with the "<--" arrow). We need to
        somehow "record" (known as "memoization" in computing) that we've
        already computed node 2 a prior when we need to compute the number of
        steps for n == 3. Enter Dynamic Programming!

        Dynamic Programming is a technique commonly used when the nature of a
        problem yields itself to the following: the solution to a given
        instance of a problem is built from the solutions to smaller problems.
        This is directly applicable to climbStairs. If we consider n to be 3,
        then to get to step 3, we can either climb from 2 to 3 (1 step) or jump
        from 1 to 3 (2 steps).

        There are two important observations from this: 1) the word "or" and 2)
        how we got to step 2 (or step 1) is not important; what matters is that
        we can get to step 3 (from 1 step). The word "or" here implies the
        solution to a current instance is the *sum* of smaller instances; we
        can get to step 3 from step 2 or step 1, which means that the number of
        ways to get to step 3 must be the sum of the number of ways to get to
        step 2 and step 1. This observation leads us to our solution.

        Encoding this observation is straightfoward: we will create an array of
        size n (the solution below uses n + 1 to emulate a 1-indexed array,
        instead of 0-indexed, which makes interpretation a little more natural)
        which will encode the following: the value at index i will be the
        number of ways to reach step i. Therefore, when i == n, we will return
        the desired solution.

        We initialize the first index with 1 (representing step 1) and the
        second index with 2 (representing step 2). This is because there is only
        one way to get to step 1 (1 step), while there are two ways to get to
        step 2 (1 step + 1 step or 2 steps). Then, we will (linearly) compute
        the following:

                        array[i] = array[i - 1] + array[i - 2]

        As we discussed above, the insight to draw from climbStairs is that the
        solution to the number of ways to reach step i is the sum of the number
        of ways to reach the step immediatley preceeding it (ie, i - 1) plus
        the number of ways to to reach two steps underneath i (ie, i - 2).
        """
        return 1 if n == 1 else 2 if n == 2 else self.dynamicProgramming(n)

    def dynamicProgramming(self, n: int) -> int:

        # initialize our memoized array
        subProblems = [0] * (n + 1)

        # initialize our base cases
        subProblems[1] = 1
        subProblems[2] = 2

        # the solution to n is the sum of prior subproblems
        for i in range(3, n + 1):
            subProblems[i] = subProblems[i - 1] + subProblems[i - 2]
        return subProblems[n]


if __name__ == "__main__":
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
# @lc code=end
