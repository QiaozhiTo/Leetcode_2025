class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neiMap = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neiMap[pattern].append(word)
        visiting = set([beginWord])
        q = deque([beginWord])
        res = 1 
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nei in neiMap[pattern]:
                        if nei not in visiting:
                            q.append(nei)
                            visiting.add(nei)
            res +=1
        return 0
        