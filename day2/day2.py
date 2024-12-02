import numpy as np

with open('input.txt', 'r') as f:
  lines = f.readlines()

def isSafe(lev):
    prec = lev[0]
    dec = lev[0] > lev[1]
    for i in lev[1:]:
        if ((i > prec) and dec):
            return False
        elif i < prec and (not dec):
            return False
        elif (abs(i-prec) < 1 or abs(i-prec) > 3):
            return False
        else:
            prec = i

    return True

count = 0
for i in lines:
    s = np.array(i.split(" "), dtype = int)
    if(isSafe(s)):
        count+=1
    else:
        for j in range(len(s)):
            new = s[:j].tolist()
            new.extend(s[j+1:])
            if isSafe(new):
                count += 1
                break
