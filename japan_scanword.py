'''
width = int(input("Input a width of the picture: "))
hight = int(input("Input a hight of the picture: "))
i = 0
string = ""
picture = []
while i != hight:
    string = input("String #" + str(i) + " ('#' is a full cell. Widht should be = " + str(width) + "): ")
    if string == "stop":
        break
    picture += [string]
    i += 1

for i in picture:
    print(i)

row = [None] * hight

print("check empty row: " + str(row)) #check
'''

picture = ["#~####~#~#",  #temp
"_#~~~~#~##",
"#~~######_",
"##_###___#", 
"_#__#_#_##", 
"_##_#_####", 
"#####_____",
"____##_##_",
"__________",
"##########"]

print(picture)
width = len(picture[0]); hight = len(picture) #temp

table = []
for i in range(hight):
    table.append([0 for j in range(width)])

for i in range(hight):
    for j in range(width):
        if picture[i][j] == '#':
            table[i][j] = 1

'''
[[1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
[0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
[1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
[1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
[0, 1, 0, 0, 1, 0, 1, 0, 1, 1],
[0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
'''

def addion_of_ones(list_row):     # Makes list of sums of consecutive ones
    #list_row = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1] 			
    rez = 0
    c = 0
    row = []
    for i in list_row:
        if i == 1:
            rez += 1
            if c == (len(list_row) - 1):
                row.append(rez)
        elif i == 0 and rez > 0:
            row.append(rez)
            rez = 0
        c += 1		
    return(row)
	


table_transposed = []
for i in range(width):           # MAKES MATRIX OF ZEROES FOR FUTURE TRANSPOSED MATRIX
    table_transposed.append([0 for j in range(hight)])
	
for j in range(width):                # THIS BLOCK TRANSPOSES THE MATRIX table
    for i in range(len(table)):
        print(table[i][j], end='')
        table_transposed[j][i] = table[i][j]
    print()

for i in table:
    print(addion_of_ones(i))
	
	
for i in table_transposed:
    print(addion_of_ones(i))

'''
    row[h] = []
    rez_h = 0
    for w in range(len(picture[h])):
        column[w] = []
        rez_w = 0
        if picture[h][w] == "#":
            rez_h += 1
            rez_w += 1
            if w == len(picture[h]) - 1:
                row[h].append(rez_h)
        elif rez_h > 0:
            row[h].append(rez_h)
            rez_h = 0
'''

