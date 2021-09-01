i = 0
while i <= 10:
    print(i)
    i = i + 1

for i in range(11):
    print(i)

# Racquetball
score_A = 0
score_B = 0
while not (score_A == 15 or score_B == 15):
    # continue playing
    pass

a = 0
b = 0
# with shutouts
while not (a == 15 or b == 15 or
           (a == 7 and b == 0) or
           (a == 0 and b == 7)):
    # continue playing
    pass

# Volleyball
while not (a >= 15 and a - b >= 2) or (b >= 15 and b - a >= 2):
    # continue playing
    pass

# another way to write it
while not (a >= 15 or b >= 15) and abs(a - b) >= 2:
    # continue playing
    pass

# Boolean Algebra
# ---------------------------------------
# | Reg algebra |     Boolean algebra   |
# |  a * 0 = 0  |  a and false == false |
# |  a * 1 = a  |  a and true == a      |
# |  a + 0 = a  |  a or false == a      |
# ---------------------------------------

# ( a or True ) == True

# They distribute like algebra.
# ( a or (b and c) ) == ( (a or b) and (a or c) )
# ( a and (b or c) ) == ( (a and b) or (a and c) )

# Double negative cancels.
# ( not (not a) ) == a

# DeMorgan's laws
# ( not (a or b) ) == ( (not a) and (not b) )
# ( not (a and b) ) == ( (not a) or (not b) )
