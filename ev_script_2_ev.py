import math
class ClassEv():

    def desired(bas, ev1, iv, opt, lvl, des, mod):
        d = ((2 * bas [opt + 1] + iv [opt + 1] + (ev1[opt + 1] / 4)) * lvl / 100)
        return math.trunc((((des / mod) - (d)) * 400 / lvl) / 4) * 4