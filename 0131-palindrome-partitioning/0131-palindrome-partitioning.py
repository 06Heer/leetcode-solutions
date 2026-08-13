class Solution:
    def partition(self, s):
        result = []
        path = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        def backtrack(start):

            # We have reached the end of the string
            if start == len(s):
                result.append(path[:])
                return

            # Try every possible substring
            for end in range(start, len(s)):

                # Only choose palindrome substrings
                if isPalindrome(start, end):

                    # Choose
                    path.append(s[start:end + 1])

                    # Explore
                    backtrack(end + 1)

                    # Undo the choice
                    path.pop()

        backtrack(0)

        return result