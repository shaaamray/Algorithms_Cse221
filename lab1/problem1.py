def isPalindrome(word):
    if word == None:
        return "and {} is not a palindrome".format(word)
    N = len(word)
    i = 0
    while i<N//2:
        if word[i] != word[N-1-i]:
            return "and {} is not a palindrome".format(word)
        i += 1
    return "and {} is a palindrome".format(word)

def isParity(number):
    if "." in number:
        return "{} cannot have parity ".format(number)
    if int(number)%2 == 0:
        return "{} has even parity ".format(number)
    else:
        return "{} has odd parity ".format(number)
    
fi = open("input.txt","r")
fo = open("output.txt","w")
fr = open("record.txt","w")
oddCount = 0
evenCount = 0
noParityCount = 0
palinCount = 0
noPalinCount = 0
allCount = 0
inputArray = []
for i in fi:
    inputArray.append(i)
for i in inputArray:
    allCount += 1
    newArray = i.split(" ")
    part1 = isParity(newArray[0])
    checkArray = newArray[1].split("\n")
    part2 = isPalindrome(checkArray[0])
    fo.write(part1+part2+"\n")
    
    if "is not a palindrome" in part2:
        noPalinCount += 1
    else:
        palinCount += 1
        
    if "has even parity" in part1:
        evenCount += 1
    elif "has odd parity" in part1:
        oddCount += 1
    elif "cannot have parity" in part1:
        noParityCount += 1
        
percentage_odd_parity = (oddCount/allCount) * 100
percentage_even_parity = (evenCount/allCount) * 100
percentage_no_parity = (noParityCount/allCount) * 100
percentage_palindrome = (palinCount/allCount) * 100
percentage_no_palindrome = (noPalinCount/allCount) * 100

fr.write("Percentage of odd parity: "+str(percentage_odd_parity)+"%\n")
fr.write("Percentage of even parity: "+str(percentage_even_parity)+"%\n")
fr.write("Percentage of no parity: "+str(percentage_no_parity)+"%\n")
fr.write("Percentage of palindrome: "+str(percentage_palindrome)+"%\n")
fr.write("Percentage of non-palindrome: "+str(percentage_no_palindrome)+"%\n")

fi.close()
fo.close()
fr.close()


    