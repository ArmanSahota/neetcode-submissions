class Solution:
    def confusingNumber(self, n: int) -> bool:
        hashmap = {0 : 0, 1: 1, 2 : None, 3 : None, 4: None, 5 : None, 6 : 9, 7: None, 8 : 8, 9 : 6}
        Ns = str(n)
        res = ""
        for i in Ns:
            if hashmap[int(i)] == None:
                return False
            res += str(hashmap[int(i)])
        res = res[:: -1]

        return res != str(n)

        