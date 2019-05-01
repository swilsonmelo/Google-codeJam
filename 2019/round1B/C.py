from sys import stdin

def main():
    cases = int(stdin.readline().strip())
    for c in range(cases):
        n,k = [int(x) for x in stdin.readline().strip().split()]
        C = [int(x) for x in stdin.readline().strip().split()]
        D = [int(x) for x in stdin.readline().strip().split()]
        res = 0
    
        for i in range(n):
            for j in range(n):
                if i <= j and abs(C[i]-D[j]) = k:
                    print(i+1,j+1)
                    res += 1

        print("Case #"+str(c+1)+":",res)



main()