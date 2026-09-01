class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)

        string_builder = []

        for char in order:
            if char in s_count:
                string_builder.extend([char] * s_count[char])

                del s_count[char]
        
        for char, count in s_count.items():
            string_builder.extend([char] * count)

        return "".join(string_builder)