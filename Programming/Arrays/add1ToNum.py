class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        ans = [1]
        i=0
        while i < len(A)-1 and A[i] == 0:
            i += 1
        A = A[i:]
        if A[-1] != 9:
            A[-1] += 1
            return A
        else:
            n = len(A)-1
            while A[n] == 9 and n > -1:
                A[n] = 0
                n -= 1
            if n == -1 and A[0] == 0:
                ans.extend(A)
                return ans
            else:
                A[n] += 1
                return A