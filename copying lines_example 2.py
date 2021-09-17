number = int(input('Введите количество диапазанов:'))

d = {}

for i in range(number):
    lst = []
    for char in input().split():
        lst.append(char)
        d[i] = lst
    print(d)

with open('source_text.txt', 'r') as f1:
    with open('new_text.txt', 'a') as f2:

        val = []
        for key in d:
            print(key)

            for i in range(int(d[key][0]), int(d[key][1]) + 1):
                val.append(i)
            print(val)

        for n, line in enumerate(f1):
            if (n + 1) in val:
                f2.write(str(line))
