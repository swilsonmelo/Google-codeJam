from sys import stdin
import sys
sys.setrecursionlimit(10000)

def solve(x,y,res):
    if( x == n-1 and y == n-1):
        print(res)
        return True
    if( x >= n or y >= n):
        return False
    if(mat[x][y] == -1):
        if(mat[x+1][y] != -1):
            t = solve(x+1,y,res+"S")
            if t:
                return t
        if(mat[x][y+1] != -1):
            t = solve(x,y+1,res+"E")
             
            if t:
                return t
    else:
        t = solve(x+1,y,res+"S")
        if t:
            return t
        t = solve(x,y+1,res+"E")
        if t:
            return t
        

def main():
    global mat,n
    cases = int(stdin.readline().strip())
    for c in range(cases):
        print("Case #"+str(c+1)+": ",end="")
        n = int(stdin.readline().strip())
        mat = [[0 for j in range(n+3)] for i in range(n+3)]
        steps = stdin.readline().strip()
        x = y = 0
        mat[x][y] = -1
        for i in range(len(steps)):
            if(steps[i] == "S"):
                x += 1
            else:
                y += 1
            mat[x][y] = -1
        """
        for i in mat:
            print(i)
        """
        solve(0,0,"")
            

main()
