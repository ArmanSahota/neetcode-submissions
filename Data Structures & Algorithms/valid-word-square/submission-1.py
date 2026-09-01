class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        Row = len(words)
        Cols = len(words[0])
        rowlist = defaultdict(list)
        collist = defaultdict(list)

        for R in range(Row):
            for C in range(len(words[R])):
                if words[R][C]: rowlist[R].append(words[R][C])
                if words[R][C]: collist[C].append(words[R][C])
        return rowlist == collist