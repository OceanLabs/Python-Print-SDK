di = {'yes': {'go':'laugh','stay':'ok','put':['the', 'money', 'in', 'the', 'bag']}, 'no': {'go': 'fun','dont go':'yeah','deliver':['cash', 'money', 'millionare']}}

target = 'go'

answer = []
if 'yes' in di.keys():
    print('works')

for i in range(0, len(di)):
    if target in di.keys()[i]:
        answer.append(di[i])
                
    for u in range(0, len(di)):
        if target in di[i][u].keys():
            answer.append(di[i][u])
            
        for o in range(0, len(di)):
            if target in di[i][u][o].keys():
                answer.append(di[i][u][o])

print(answer)

##di.keys()
##di['yes'].keys()
##di['yes']['put']
