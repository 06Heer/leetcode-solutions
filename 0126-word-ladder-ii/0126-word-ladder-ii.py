from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # parents[word] = all words that can reach word
        # through a shortest path
        parents = defaultdict(set)

        queue = deque([beginWord])

        # Words that have already been visited
        visited = {beginWord}

        found = False

        while queue and not found:

            level_visited = set()

            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == word[i]:
                            continue

                        next_word = word[:i] + ch + word[i + 1:]

                        if next_word not in wordSet:
                            continue

                        # First time we see this word
                        if next_word not in visited:
                            if next_word not in level_visited:
                                level_visited.add(next_word)
                                queue.append(next_word)

                            parents[next_word].add(word)

                        # Already discovered at the same BFS level
                        elif next_word in level_visited:
                            parents[next_word].add(word)

                        if next_word == endWord:
                            found = True

            visited.update(level_visited)

        if endWord not in parents:
            return []

        # DFS / Backtracking to construct all paths
        result = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()

        backtrack(endWord)

        return result