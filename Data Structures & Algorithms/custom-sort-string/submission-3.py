class Solution:
    def customSortString(self, order: str, s: str) -> str:
        string = []
        count = Counter(s)

        for char in order:
            if char in count:
                string.extend((char) * count[char])
            
                del count[char]
        
        for char, c in count.items():
            string.extend((char) * c)

        return "".join(string)