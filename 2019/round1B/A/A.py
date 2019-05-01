from sys import stdin

def main():
    cases = int(stdin.readline().strip())
    for c in range(cases):
        N,K = [int(x) for x in stdin.readline().strip().split()]
        
        x = y = 0
        for i in range(N):
            d = i
            d = [x for x in stdin.readline().strip().split()]
            d[0] = int(d[0])
            d[1] = int(d[1])
            if(d[2] == "N" and y < d[1]):
                y = d[1] + 1
            if(d[2] == "S" and y > d[1]):
                y = d[1] - 1
            if(d[2] == "E" and x < d[0]):
                x = d[0] + 1
            if(d[2] == "W" and x > d[0]):
                x = d[0] - 1
        
        if( x >= K): x = K-1
        if( x < 0): x = 0
        if( y >= K): y = K-1
        if( y < 0): y = 0
        print("Case #"+str(c+1)+":",x,y)
        
    

main()