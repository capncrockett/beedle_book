# cube_field.py
from random import random
# https://math.stackexchange.com/questions/1066981/standing-at-the-center-of-a-cube-and-walking-halfway-to-a-wall-field-of-vision?newreg=00561040f0374a51861611ef53fbc34d

total = 5000
hits = 0

for i in range(total):
    u = random()
    v = random()
    w = random()
    if u > 0 and abs(v) < 2 * u and abs(w) < 2 * u:
        hits = hits + 1

print(hits/total)
