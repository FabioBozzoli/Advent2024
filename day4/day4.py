import re
import numpy as np

with open('input.txt', 'r') as f:
  lines = f.readlines()

hr = [] #horizontal-right
hl = [] #horizontal left
for i in lines:
    hr.append(re.findall("XMAS", i))
    hl.append(re.findall("SAMX", i))

count = 0
for i in hr:
    count += len(i)
for i in hl:
    count += len(i)

rows_char = []
for i in lines:
    cols = []
    for j in range(len(i)):
        if j != len(lines):
          cols.append(i[j])

    rows_char.append(cols)

rows_transposed = (np.char.array(rows_char))
rows_transposed = rows_transposed.transpose()

rows = []
for i in rows_transposed:
    rows.append("".join(i))

vu = [] #vertical-up
vd = [] #vertical-down

for i in rows:
    vu.append(re.findall("XMAS", i))
    vd.append(re.findall("SAMX", i))

for i in vu:
    count += len(i)
for i in vd:
    count += len(i)

rows_char_np = np.array(rows_char)
diag = []
for i in range(-136,137):
    diag.append("".join(rows_char_np.diagonal(i)))

dl = [] #vertical-up
dr = [] #vertical-down

for i in diag:
    dl.append(re.findall("XMAS", i))
    dr.append(re.findall("SAMX", i))

for i in dl:
    count += len(i)
for i in dr:
    count += len(i)

rows_char_flip = np.fliplr(rows_char_np)

diag_flipped = []
for i in range(-136,137):
    diag_flipped.append("".join(rows_char_flip.diagonal(i)))

adl = [] #vertical-up
adr = [] #vertical-down

for i in diag_flipped:
    adl.append(re.findall("XMAS", i))
    adr.append(re.findall("SAMX", i))

for i in adl:
    count += len(i)
for i in adr:
    count += len(i)

print(count)

#TASK2
count =0
for i in range(len(rows)-2):
    for j in range(len(rows[0])-2):
        if(rows_char[i][j] == 'M' and rows_char[i+1][j+1]=='A' and rows_char[i+2][j+2] == 'S'):
            if(rows_char[i][j+2] == 'M' and rows_char[i+2][j] == 'S'):
                count += 1
            elif(rows_char[i][j+2] == 'S' and rows_char[i+2][j] == 'M'):
                count += 1
        elif(rows_char[i][j] == 'S' and rows_char[i+1][j+1] == 'A' and rows_char[i+2][j+2] == 'M'):
            if(rows_char[i][j+2] == 'M' and rows_char[i+2][j] == 'S'):
                count += 1
            elif(rows_char[i][j+2] == 'S' and rows_char[i+2][j] == 'M'):
                count += 1

print(count)
