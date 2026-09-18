class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for i in strs:
            result.append(str(len(i)) + '#' + i)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        j = 0
        i = 0
        while i != len(s):
            while s[j] != '#':
                j += 1
            number = int(s[i : j])
            i = j + 1
            j += number + 1
            result.append(s[i : j])
            i = j
        return result


