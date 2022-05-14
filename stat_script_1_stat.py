import math
class ClassStat():

    def HPReturn(bas, iv, ev1, lvl):
        return math.trunc((((2 * bas[1] + iv[1] + (ev1[2] / 4)) * lvl) / 100) + lvl + 10)

    def atkReturn(bas, iv, ev1, lvl, atknat):
        return math.trunc((((((2 * bas[2] + iv[2] + (ev1[2] / 4)) * lvl) / 100) + 5) * atknat))

    def defReturn(bas, iv, ev1, lvl, defnat):
        return math.trunc((((((2 * bas[3] + iv[3] + (ev1[3] / 4)) * lvl) / 100) + 5) * defnat))

    def satkReturn(bas, iv, ev1, lvl, satknat):
        return math.trunc((((((2 * bas[4] + iv[4] + (ev1[4] / 4)) * lvl) / 100) + 5) * satknat))  

    def sdefReturn(bas, iv, ev1, lvl, sdefnat):
        return math.trunc((((((2 * bas[5] + iv[5] + (ev1[5] / 4)) * lvl) / 100) + 5) * sdefnat))

    def sReturn(bas, iv, ev1, lvl, snat):
        return math.trunc((((((2 * bas[6] + iv[6] + (ev1[6] / 4)) * lvl) / 100) + 5) * snat))  