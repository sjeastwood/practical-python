# bounce.py
#
# Exercise 1.5

height = 100 #metres

max_bounces = 10 #maximum number of bounces

bounce = 0


while bounce < max_bounces:
    height *= (3/5)
    bounce += 1
    height = round(height, 4)
    print(bounce, height)
