def LCS(X, Y):
    m = len(X)
    n = len(Y)
    my_arr = [[0 for x in range(n+1)] for x in range(m+1)]
    for j in range(m+1):
        for k in range(n+1):
            if j == 0 or k == 0:
                my_arr[j][k] = 0
            elif X[j-1] == Y[k-1]:
                my_arr[j][k] = my_arr[j-1][k-1] + 1
            else:
                my_arr[j][k] = max(my_arr[j-1][k], my_arr[j][k-1])

    pos = my_arr[m][n]
    val = pos
    LCS = [""] * (pos+1)
    LCS[pos] = ""

    j = m
    k = n
    while j > 0 and k > 0:
        if X[j-1] == Y[k-1]:
            LCS[pos-1] = X[j-1]
            j -= 1
            k -= 1
            pos -= 1
        elif my_arr[j-1][k] > my_arr[j][k-1]:
            j -=1
        else:
            k -=1
            
    LCS.pop()
    correctness = (val * 100) // 8
    LCS.append(correctness)
    return LCS
            
file_input = open('input1.txt', 'r')
file_output = open('output1.txt', 'w')

my_arr2 = []

for k in file_input:
    my_arr2.append(k.replace('\n',''))
    
zones = my_arr2[0]
case1 = my_arr2[1]
case2 = my_arr2[2]
value = LCS(case1, case2)
d = {
            "Y": "Yasnaya",
            "P": "Pochinki",
            "S": "School",
            "R": "Rozhok",
            "F": "Farm",
            "M": "Mylta",
            "H": "Shelter",
            "I": "Prison"
}
correctness = value.pop()

for k in value:
    if k in d:
        file_output.write(str(d[k])+" ")
file_output.write('\n')
file_output.write("Correctness of prediction: "+str(correctness)+"%")

file_input.close()
file_output.close()