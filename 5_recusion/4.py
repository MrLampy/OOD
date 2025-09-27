def waterfall(original:list, y : int, x: int):
    old = original[y][x]
    original[y][x] = 0
    if y > 0 and old >= original[y-1][x] and original[y-1][x] != 0:
        waterfall(original,y-1,x)
    if x < column and old >= original[y][x+1] and original[y][x+1] != 0:
        waterfall(original,y,x+1)
    if x > 0 and old >= original[y][x-1] and original[y][x-1] != 0:
        waterfall(original,y,x-1)
    if y < row and old >= original[y+1][x] and original[y+1][x] != 0:
        waterfall(original,y+1,x)

print(' *** Water Flow ***')
bound, user_input, start = input('Input rows,cols/data1,data2,.../start_row,start_col : ').split('/')
bound1, bound2 = bound.split(',')
bound1,bound2 = int(bound1),int(bound2)
start = start.split(',')
start1,start2 = int(start[0]),int(start[1])
user_input = user_input.split(',')
main = []
for r in range(bound1):
    main.append([])
    for c in range(bound2):
        main[r].append(int(user_input[r][c]))
row = 0
column =  0
if bound1 not in range(1,10) or bound2 not in range(1,10):
    print('Error: Rows and columns must be between 1 and 9')
elif bound1<=start1 or bound2<=start2:
    print('Error: Start coordinates are out of grid bounds')
else:
    row = len(main)-1
    column = len(main[0])-1
    waterfall(main,start1,start2)
    for i in range(row+1):
        for ii in range(column+1):
            print(main[i][ii], end='')
        print()

# Note4me: ถ้าไม่อยากให้ใช้ loop ตอน input/output อาจจะต้องใช้เป็น list แล้ว pop() เอา