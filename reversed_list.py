data = [4, 2, 567, 108, 8, 123, 35, 145, 890, 156, 987, 100, 200, 178]
min_val = 100
max_val = 200

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if (value <= 100) or (value >= 200):
        del data[top_index - index]
        # print(value)
        print(data)
        