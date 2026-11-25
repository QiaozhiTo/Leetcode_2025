class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        wordMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                wordMap[pattern].append(word)
        
        q = deque([beginWord])
        visit = set(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in wordMap[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            
            res += 1
        return 0
