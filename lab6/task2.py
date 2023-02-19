def LCS(X, Y, Z):
    m = len(X)
    n = len(Y)
    o = len(Z)
    my_arr = [[[0 for k in range(o+1)] for j in range(n+1)] for i in range(m+1)]

    for k, p in enumerate(X):
        for j, s in enumerate(Y):
            for i, g in enumerate(Z):
                if p == s and s == g:
                    my_arr[k+1][j+1][i+1] = my_arr[k][j][i] + 1
                else:
                    my_arr[k+1][j+1][i+1] = max(my_arr[k+1][j+1][i],my_arr[k][j+1][i+1],my_arr[k+1][j][i+1])
    string = ""
    while m > 0 and n > 0 and o > 0:
        count = my_arr[m][n][o]
        if count == my_arr[m-1][n][o]:
            m -= 1
        elif count == my_arr[m][n-1][o]:
            n -= 1
        elif count == my_arr[m][n][o-1]:
            o -= 1
        else:
            string += str(X[m-1])
            m -= 1
            n -= 1
            o -= 1
    return len(string[::-1])

file_input = open('input2.txt', 'r')
file_output = open('output2.txt', 'w')
value = []

for i in file_input:
    value.append(i.replace('\n',''))
case1 = value[0]
case2 = value[1]
case3 = value[2]

span = LCS(case1, case2, case3)

file_output.write(str(span))
file_input.close()
file_output.close()