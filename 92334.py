import sys
import ast

sysdata1 = sys.stdin.readline().rstrip()
sysdata2 = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline().rstrip())

id_list = ast.literal_eval(sysdata1)
report = ast.literal_eval(sysdata2)

singo_info = {}
singo_cnt = {}
answer = [0 for _ in range(len(id_list))]  # id_list 별 메일받은 횟수

for index in range(len(id_list)):
    singo_info[id_list[index]] = {
        'id': id_list[index], 'idIndex': index,  'singoList': [], 'stopID': []}
    singo_cnt[id_list[index]] = 0


for item in report:
    id = item.split()
    singoja = id[0]
    singoedId = id[1]
    singo_info[singoja]['singoList'].append(singoedId)


for singoja in singo_info:
    singo_info[singoja]['singoList'] = list(set(singo_info[singoja]['singoList']))
    singo_info = singo_info[singoja]['singoList'] 
    for singoedId in singoList:
        singo_cnt[singoedId] += 1

for singoja in singo_info:
    singoList = singo_info[singoja]['singoList']
    singoIndex = singo_info[singoja]['idIndex']
    for singoedId in singoList:
        if (singo_cnt[singoedId] >= k):
            singo_info[singoja]['stopID'].append(singoedId)

for singoja in singo_info:
    stopIdCnt = len(singo_info[singoja]['stopID'])
    answer[singo_info[singoja]['idIndex']] = stopIdCnt
    
print(answer)
 
