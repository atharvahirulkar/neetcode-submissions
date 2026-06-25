class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        check = []
        fleet = 1
        for p,s in cars:
            ar_time = (target - p) / s

            if not check or ar_time > check[-1]:
                check.append(ar_time)

        return len(check)

