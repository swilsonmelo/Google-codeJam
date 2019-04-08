from sys import stdin


def convertRight(n):
    m = [i for i in str(n)]
    pos = len(m)-1
    t = True
    for i in range(len(m)):
        if(not t):
            m[i] = "9"
        if(m[i] == "4" and t):
            m[i] = "3"
            t = False
    return int("".join(m))

def convertLeft(n):
    m = [i for i in str(n)]
    pos = len(m)-1
    t = True
    for i in range(len(m)):
        if(not t):
            m[i] = "0"
        if(m[i] == "4" and t):
            m[i] = "5"
            t = False
    return int("".join(m))  

def haveFour(n):
    m = str(n)
    for i in m:
        if( i == "4"):
            return True
    return False


def solve(n):
    high = n-1
    low = 1
    while True:
        #print(low,high)
        if haveFour(high):
            high = convertRight(high)
        low = n - high
        if(not haveFour(low) ):
            print(low,high)
            return
        if haveFour(low):
            low = convertLeft(low)
        high = n - low
        if(not haveFour(high) ):
            print(low,high)
            return
        
        

def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        N = int(stdin.readline().strip())
        print("Case #"+str(i+1)+": ",end="")
        solve(N)
        #print(convertLeft(N))
        #print(convertRight(N))
        


main()
