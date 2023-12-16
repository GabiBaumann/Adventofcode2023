grids = [[]]
out1 = out2 = 0

with open('input--debug') as file:
    for line in file:
        if line == '\n':
            grids.append([])
        else:
            grids[-1].append(line.rstrip())

print(grids)
for grid in grids:
    leny = len(grid)
    lenx = len(grid[0])
    for y in range(leny-1):
        c = 0
        for x in range(lenx):
            if grid[y][x] != grid[y+1][x]:
                c += 1
        if c == 0:
            #mirror candidate seed. Analyse in-place?
            # kind of, for now. mebbe the step dance can join the functions
            # range to check (-1 for len, -1 for y+1 line)
            had_smudge = is_smudge = not_clean = False
            steps = min(y, leny-y-2)
            for step in range(steps):
                clean, smudge = test_rows(y-step, y+step+2)
                if smudge:
                    if had_smudge: 
                        is_smudge = False
                        break
                    else: 
                        had_smudge = True
                        is_smudge = True
                if not clean:
                    not_clean = True
            # now we should be good...
            if not not_clean:
                print('Clean mirror @', y-steps, y, y+1, y+steps+1)
                out1 += y #something...
            elif is_smudge:
                print('Smudge solution @', y-steps, y, y+1, y+steps+1)
                out2 += y #something...
        elif c == 1:
            # smudge candidate. Needs to continue as smudge-less match
            steps = min(y, leny-y-2)
            is_smudge = True
            for step in range(steps):
                clean, smudge = test_rows(y-step, y+step+2)
                if smudge:
                    is_smudge = False
                    break # would need to be clean, break 'for step'
            if is_smudge:
                print('Smudge on neighbors @', y-steps, y, y+1, y+steps+1)
                out2 += y # something, same as above.

    for x in range(lenx-1):
        c = 0
        for y in range(leny):
            if grid[y][x] != grid[y][x+1]:
                c += 1
        if c == 0:
            # mirror candidate seed.
            had_smudge = is_smudge = not_clean = False
            steps = min(x, lenx-x-2)
            for step in range(steps)
                clean, smudge = test_cols(x-step, x+step+2)
                if smudge:
                    if had_smudge:
                        is_smudge = False
                        break
                    else:
                        had_smudge = True
                        is_smudge = True
                if not clean:
                    not_clean = True
            if not not_clean:
                print('Clean mirror @', x-steps, x, y+1, x+steps+1)
                out1 += x # something
            elif is_smudge:
                print('Smudge solution @', x-steps, x, x+1, x+steps+1)
                out2 += x # something
        elif c == 1:
            # smudge candidate. aao.
            is_smudge = True
            steps = min(x, lenx-x-2)
            for step in range(steps):
                clean, smudge = test_cols(x-step, x+step+2)
                if smudge:
                    is_smudge = False
                    break
            if is_smudge:
                print('Smudge on neighbors @', x-steps, x, x+1, x+steps+1)
                out2 += y # something, aao

print(out1, out2)

