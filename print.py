def print_grid(top_numbers, left_numbers,grid):
    def printtop():
        for i in range(height):
            for _ in range(width*2):
                print(" ",end='')
            #print("|")
            for j in range(size):
                print("|",end='')
                try:
                    a=top_numbers[j][i]
                except:
                    a=" "
                print(a,end='')
            print("|",end='')
            
            print()

        pass

    def printleft():
        for i in range(size):
            print("-"*(size+width)*2)
            for j in range(width):
                try:
                    a=left_numbers[i][j]
                except:
                    a=" "
                print(a,end='')
                print(" ",end='')

            for j in range(size):
                print("|",end='')
                print(grid[i][j],end='')
            
            print("|")
            pass

    size=len(left_numbers)
    width=1
    height=1
    for i in range(size):
        width=max(width,len(left_numbers[i])) 
        height=max(height,len(top_numbers[i]))

    printtop()
    printleft()