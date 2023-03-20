# Task 3 (optional). Print the next pattern using a loop within a loop:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

string = ''

for i in range(5):
    for j in range(1, i + 2):
        if j > 1:
            string += ' '
        string += str(j)
    print(string)
    string = ''
