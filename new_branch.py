lst = [4, 33, 35, 36, 369]

for i in lst:
    count = 0
    for j in str(i):
        if j == '3' or j == '6' or j == '9':
            count += 1
    if count != 0:
        print('clap' * count)
    else:
        print('No')
