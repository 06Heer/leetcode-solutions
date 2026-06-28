class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()

        current = 1

        for i in range(1, len(arr)):
            current = min(arr[i], current + 1)

        return current