class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        lastTime = 0
        fleet = 0

        for p, s in cars:
            time = (target - p) / s
            if time > lastTime:
                fleet += 1
                lastTime = time
        return fleet


            
            