words = ['oranges', 'apples_bigApples', 'apples_smallApples', 'pears']
new_list = []
for i in range(0, len(words)):
    part_a = ''
    part_b = ''
    for u in range(0, len(words[i])):
        if words[i][u] == '_':
            part_a = words[i][0:u]
            part_b = words[i][(u+1):len(words[i])]
    if part_a != '' and part_b != '':
        new_list.append({part_a:part_b})
    else:
        new_list.append(words[i])
print new_list
for i in range(0, len(new_list)-1):
    if new_list[i]
