from television import Television

tv1 = Television('1', 1, 99, 1)
print(f'Current channel was: {tv1.channel}')
print('Changing...')
for x in range(0, 99):
    tv1.changeChannelHigher()
    print(tv1.channel)

tv2 = Television('2', 1, 23, 23)
print(f'Current channel was: {tv2.channel}')
print('Changing...')
for x in range(0, 22):
    tv2.changeChannelLower()
    print(tv2.channel)
