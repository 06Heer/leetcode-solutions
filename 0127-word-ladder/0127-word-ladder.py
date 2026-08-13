from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        # If endWord is not present, transformation is impossible
        if endWord not in wordSet:
            return 0

        queue = deque([beginWord])
        visited = {beginWord}

        length = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return length

                # Change one character at a time
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == word[i]:
                            continue

                        new_word = (
                            word[:i] +
                            ch +
                            word[i + 1:]
                        )

                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            queue.append(new_word)

            length += 1

        return 0