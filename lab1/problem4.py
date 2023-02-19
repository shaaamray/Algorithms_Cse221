fi = open("input4.txt","r")
fo = open("output4.txt","w")
matrix = []
A = []
B = []
C = []

for i in fi:
  if i.replace("\n","") != "":
    matrix.append(i.replace("\n",""))

n = int(matrix[0])
matrix = matrix[1:]

for i in range(n*2):
  if i < n:
    element = matrix[i].split(" ")
    for j in range(len(element)):
      element[j] = int(element[j])
    A.append(element)
  else:
    element = matrix[i].split(" ")
    for j in range(len(element)):
      element[j] = int(element[j])
    B.append(element)

for i in range(n):
  element = []
  for x in range(n):
    element.append(0)
  C.append(element)

for i in range(n):
  for j in range(n):
    for k in range(n):
      C[i][j] += A[i][k] * B[k][j]

for i in range(n):
  for j in range(n):
    fo.write(str(C[i][j])+" ")

  fo.write("\n")
fi.close()
fo.close()