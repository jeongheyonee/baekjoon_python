co_list = []
co_list.append(list(map(int, input().split())))
co_list.append(list(map(int, input().split())))
co_list.append(list(map(int, input().split())))

if co_list[0][0] == co_list[1][0]:
    x = co_list[2][0]
elif co_list[1][0] == co_list[2][0]:
    x = co_list[0][0]
elif co_list[0][0] == co_list[2][0]:
    x = co_list[1][0]

if co_list[0][1] == co_list[1][1]:
    y = co_list[2][1]
elif co_list[1][1] == co_list[2][1]:
    y = co_list[0][1]
elif co_list[0][1] == co_list[2][1]:
    y = co_list[1][1]

print(x, y)

