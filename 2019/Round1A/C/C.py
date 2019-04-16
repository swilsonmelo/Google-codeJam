from sys import stdin



def solve(x,y,mat,st):
    global r,c
    res = True
    """
    for i in mat:
        print(i)
    "  
    for i in range(1,r+1):
        for j in range(1,c+1):
            if mat[i][j] == False:
                res = False
            #print(i,j)
            if(  i != x and y != j ):
                if( i - j != x - y and i + j != x + y and mat[i][j] != True ):
                    moves += 1
                    #print("SI")
        if(moves):
            break
    #print(moves, 100,r)
    if(moves == 0 and res == False):
        return False
    elif moves == 0:
        print("POSSIBLE")
        for w in st:
            print(w[0],w[1])
        return True
    #print("khavfafa")
    """
    moves = 0
    for i in range(1,r+1):
        for j in range(1,c+1):
            if mat[i][j] == False:
                res = False
            #print(i,j,x,y)
            if(  i != x and y != j ):
                #print(x,y,i,j)
                if( i - j != x - y and i + j != x + y and mat[i][j] != True ):
                    moves += 1
                    mat[i][j] = True
                    res = solve(i,j,mat,st+[[i,j]])
                    if( res ):
                        return res
                    mat[i][j] = False
                    #print("moves", moves)

    if(moves == 0 and res == False):
        return False
    elif moves == 0:
        print("POSSIBLE")
        for w in st:
            print(w[0],w[1])
        return True
    
    return False
    

def main():
    global r,c
    cases = int(stdin.readline().strip())
    for c in range(cases):
        print("Case #"+str(c+1)+": ",end = "")
        r,c = [int(x) for x in stdin.readline().strip().split()]
        mat = [[False for j in range(c+1)] for i in range(r+1)]
        
        res = False
        """
        mat[1][1] = True
        res = solve(1,1,mat,[])
        """
        for i in range(1,r+1):
            for j in range(1,c+1):
                mat[i][j] = True
                res = solve(i,j,mat,[[i,j]])
                break
            if(res):
                break
        if( not res):
            print("IMPOSSIBLE")
        
        

main()
