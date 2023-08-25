import ast
import re

f = open("./input.txt", 'r')
id = f.readline().rstrip()

answer = '...!@BaT#*..y.abcdefghijklm'

answer = id.lower()
answer = re.sub(r'[^\w.-]','',answer)
answer = re.sub(r'[.]{2,}','.',answer)
answer = re.sub(r'^[.]', '', answer)
answer = re.sub(r'[.]$', '', answer)
# answer = re.sub(r'^[.]', '', answer)
# answer = re.sub(r'[.]$', '', answer)
# 위에 2개를 아래처럼 합해서 가능 ~ 
# answer = re.sub(r'^[.]|[.]$', '', answer)
answer =  'a' if len(answer) == 0 else answer
answer =  answer[:14] if len(answer) > 15 and answer[14] == '.' else answer[:15]
answer =  answer + (answer[-1] * (3 -len(answer))) if len(answer) < 3 else answer
print(answer)

