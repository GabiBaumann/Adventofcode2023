with open('input-debug') as file:
    for line in file:
        grid.append([])
        sgrid.append([])
        for c in line.rstrip():
            grid[-1].append(int(c)
            sgrid[-1].append([])
            path[-1].append([])

endy = len(grid) - 1
endx = len(grid[0]) - 1

#step 1:
sgrid[0][1].append(grid[0][1])
path[0][1].append('R')
sgrid[1][0].append(grid[1][0])
path[1][0].append('D')

#step 2:
# 1,1
a = sgrid[0][1][0]
b = sgrid[1][0][0]
if a == b:
    sgrid[1][1].append(sgrid[0][1][0] + grid[1][1])
    path[1][1].append('.')
elif a < b:
    sgrid[1][1].append(sgrid[0][1][0] + grid[1][1])
    path[1][1].append('D')
    sgrid[1][1].append(sgrid[1][0][0] + grid[1][1])
    path[1][1].append('.') #called on DDD only
else:
    sgrid[1][1].append(sgrid[1][0][0] + grid[1][1])
    path[1][1].append('R')
    sgrid[1][1].append(sgrid[0][1][0] + grid[1][1])
    path[1][1].append('.')
# 0,2
a = sgrid[0][1][0]
b = sgrid[1][1][0] + grid[1][2]
if a == b:
    sgrid[0][2].append(sgrid[0][1] + grid[0][2])
    path[0][2].append('.')
elif a < b:
    sgrid[0][2].append(a + grid[0][2])
    path[0][2].append('RR')
    sgrid[0][2].append(b + grid[0][2])
    path[0][2].append('.')
else:
    sgrid[0][2].append(b + grid[0][2])
    path[0][2].append('.')
# 2,0
a = sgrid[1][0][0]
b = sgrid[1][1][0] + grid[1][1]
if a == b:
    sgrid[2][0].append(a + grid[2][0])
    path[2][0].append('.')
elif a < b:
    sgrid[2][0].append(a + grid[2][0])
    path[2][0].append('DD')
    sgrid[2][0].append(b + grid[2][0])
    path[2][0].append('.')
else:
    sgrid[2][0].append(b + grid[2][0])
    path[2][0].append('.')

#step 3:
# 1,2
a = sgrid[0][2][0]
b = sgrid[1][1][0]
c = min(sgrid[0][2][0], sgrid[1][1][0]) + grid[2][1] + grid[2][2]
if c <= a and c <= b:
    sgrid[1][2].append(c + grid[1][2])
    path[1][2].append('.')
elif a == b:
    sgrid[1][2].append(a + grid[1][2])
    path[1][2].append('.')
elif a < b:
    sgrid[1][2].append(a + grid[1][2])
    path[1][2].append('D')
    if c <= b:
        sgrid[1][2].append(c + grid[1][2])
        path[1][2].append('.'
    else:
        sgrid[1][2].append(b + grid[1][1])

if a == b 
