import string

f = open("exp2.txt","a+")
label = ["Pg1","FOUR","FIVE","TEMP"]
stmt = ["START","USING"]
stmt2 = ["L","A","ST","DC","DS","END"]
op = ["*","1","2","H","F", "TEMP", "BASE", "FOUR"]

lc = 0
b = 0
updateLC = 0
convert2list = []
operands = []
operandscopy = []

with open("exp2.txt", "r") as file:
    for line in file:
        s = line.split('|')
        for i in s:
            i = str(i).replace(" ", "")
            i = str(i).replace("\n", "")
            convert2list.append(i)
# print(convert2list)

st = open("symboltable.txt","w+")
st.write("Symbol | Value | Length | R/A\n")
pass1 = open("pass1.txt", "w+")
pass1.write("LC\t\n")
lt = open("literal.txt", "w+")
lt.write("Literal | Value | Length | R/A \n")

for i in range(3, len(convert2list)):
    if (i % 3 - 2) == 0:
        operandscopy.append(convert2list[i].split(","))
    
for i in range(3, len(convert2list)):
    if convert2list[i] == 'END':
        pass1.write(str(lc))
        break
    if (i % 3 - 2) == 0:
        a = 0
        operands.append(convert2list[i].split(","))
        if operands[a][0] == "1":
            updateLC = 4
        elif operands[a][0] == 'F':
            updateLC = 4
        elif operands[a][0] == 'B':
            updateLC = 1
        elif operands[a][0] == 'H':
            updateLC = 2
        elif operands[a][0] == 'D':
            updateLC = 8
        elif  operands[a][0] == '_' or operands[a][0] == '*':
            updateLC = 4
            pass1.write('0\n')
        operands.pop()

    if(i % 3 - 1) == 0:
        if convert2list[i] in stmt2:
            lc = updateLC + lc
            pass1.write(str(lc))
            pass1.write("\t\t")
            if str(operandscopy[b+2][1]) == 'FOUR' or str(operandscopy[b+2][1]) == 'FIVE' or str(operandscopy[b+2][1]) == 'TEMP'  :
                pass1.write(convert2list[i])
                pass1.write("\t\t1,_\n")
            elif str(operandscopy[b+2][1]) == 'F' or str(operandscopy[b+2][1]) == 'D' :
                pass1.write("__\n")
            else:
                pass1.write(operandscopy[b+2][1])
                pass1.write("\n")
            b += 1
                
    if i % 3 == 0:
        if convert2list[i%3+5] == "_":
            RA = "R"
        else:
            RA = "A"
        if  convert2list[i] in label:
            st.write(convert2list[i])
            st.write("\t|\t")
            st.write(str(lc))
            st.write("\t|\t")
            if updateLC == 0:
                updateLC = 1
                st.write(str(updateLC))
            else:
                st.write(str(updateLC))
            st.write("\t|\t")
            st.write(RA)
            st.write('\n')
        

for i in range(0, len(operandscopy)):
    if convert2list[i%3+4] == "_":
            RA = "R"
    elif convert2list[i%3+5] == "_":
            RA = "R"
    else:
            RA = "A"
    if operandscopy[i][0] == "F" or operandscopy[i][0] == "H" or operandscopy[i][0] == "D":
        # print(operandscopy[i])
        updateLC = 4
        lc = updateLC + lc
        str1 = ","
        word = str1.join(operandscopy[i])
        lt.write(word)
        lt.write("\t\t|\t")
        lt.write(str(lc))
        lt.write("\t|\t")
        lt.write(str(updateLC))
        lt.write("\t|\t")
        lt.write(RA)
        lt.write("\n")

    if operandscopy[i][0] == "H":
        updateLC = 2

pass1.close()
st.close()
lt.close()
st2list = []
with open('symboltable.txt', 'r') as file:
    for line in file:
        s = line.split('|')
        for i in range(0, len(s)):
            s[i] = s[i].replace('\n', '')
            s[i] = s[i].replace(' ', '')
            s[i] = s[i].replace('\t', '')
            if(i % 4 == 0 or i % 4 - 1 == 0):
                st2list.append(s[i])
def list2dictonary(lst): 
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
    return res_dct
dict = list2dictonary(st2list)
# print(dict)
b = 0
lc = 0
pass2 = open("pass2.txt", "w+")
pass2.write("LC\t\n")
for i in range(0, len(convert2list)):
    if(i % 3 - 1) == 0:
        if convert2list[i] in stmt2:
            # print(convert2list[i])
            lc = updateLC + lc
            pass2.write(str(lc))
            pass2.write("\t\t")
            if str(operandscopy[b+2][1]) == 'FOUR' or str(operandscopy[b+2][1]) == 'FIVE' or str(operandscopy[b+2][1]) == 'TEMP'  :
                pass2.write(convert2list[i])
                pass2.write("\t\t"+dict[str(operandscopy[b+2][1])]+"\n")
            
            elif str(operandscopy[b+2][1]) == 'F' or str(operandscopy[b+2][1]) == 'D' :
                pass2.write("__\n")
            else:
                pass2.write(operandscopy[b+2][1])
                pass2.write("\n")
            b += 1

pass2.close()

pass1 = open('pass1.txt', 'r')
print("\nPass1 table")
if pass1.mode == 'r':
    print(pass1.read())
pass1.close()
pass2 = open('pass2.txt', 'r')
print("\nPass2 table")
if pass1.mode == 'r':
    print(pass2.read())
pass2.close()
st = open('symboltable.txt', 'r')
print("\nSymbol Table")
if st.mode == 'r':
    print(st.read())
st.close()
lt = open('literal.txt', 'r')
print("\nLiteral Table")
if lt.mode == 'r':
    print(lt.read())
lt.close()

