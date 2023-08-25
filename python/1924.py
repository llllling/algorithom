import sys
x, y = map(int,sys.stdin.readline().rstrip().split())
sum = 0
for i in range(1, x) :
    if ( i == 1 or i == 3 or i == 5 or i ==7 or
        i == 8 or i == 10 or i == 12 ):
        sum += 31
    elif i == 4 or i == 6 or i == 9 or i == 11 :
        sum += 30
    elif i == 2 :
        sum += 28

sum += y
result = sum % 7

if result == 0 :
    print("SUN")
elif result == 1 :
    print("MON")
elif result == 2 :
    print("TUE")
elif result == 3 :
    print("WED")
elif result == 4 :
    print("THU")
elif result == 5 :
    print("FRI")
elif result == 6 :
    print("SAT")

