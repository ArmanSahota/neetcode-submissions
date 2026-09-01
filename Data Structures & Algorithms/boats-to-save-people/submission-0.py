class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        L = 0
        R = len(people) - 1
        boat = 0
        people.sort()
        while L <= R:
            if people[L] + people[R] <= limit:
                L += 1
            R -= 1
            boat += 1
        return boat
            




        