class ClimbingStairsSolutions:
    def climb_stairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        s1 = 1
        s2 = 2
        t = 0
        for _ in range(2, n):
            t = s1 + s2
            s1 = s2
            s2 = t
        return t