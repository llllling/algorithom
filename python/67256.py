import ast

f = open("./input.txt", 'r')
list1 = f.readline().rstrip()
hand = f.readline().rstrip()
f.close()
numbers = ast.literal_eval(list1)
answer = ''
keypad = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
L = [4, -1]
R = [4, -1]

def check(number) :
    return number == 2 or number == 5 or number == 8 or number == 0

for i in range(len(numbers)) : 
    index = numbers[i] - 1
    k = keypad[index]
    if numbers[i] == 1 or numbers[i]  == 4 or numbers[i] == 7 :
        answer += 'L'
        L =  [k, numbers[i]]  
    elif numbers[i] == 3 or numbers[i]  == 6 or numbers[i] == 9 :
        answer += 'R'
        R =  [k, numbers[i]]
    else :
        absL = abs(L[0] - k)
        if check(L[1]) :
            absL -= 1
        absR = abs(R[0] - k)
        if check(R[1]) :
            absR -= 1
        if absL  < absR :
           answer += 'L'
           L =  [k, numbers[i]]
        elif absL > absR :
           answer += 'R'
           R =  [k, numbers[i]]
        else : 
            if hand == 'right' :
                answer += 'R'
                R =  [k, numbers[i]]
            else : 
                answer += 'L'
                L =  [k, numbers[i]]  
print(answer)

