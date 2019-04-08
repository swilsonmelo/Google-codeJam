#include<bits/stdc++.h>
#define N 10
#define M 20
using namespace std;

int mat[N][N];
int n;

int main(){
    freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int cases;
    scanf("%d",&cases);
    for(int c = 1; c <= cases; c++){
        memset(mat,0,sizeof mat);

        scanf("%d",&n);
        char steps[M];
        scanf("%s",&steps);
        int x,y;
        x = 0;
        y = 0;
        printf("steps: %s\n",steps);
        mat[x][y] = -1;
        for(int i = 0; i < strlen(steps); i++){
            if(steps[i] == 'S'){
                x++;
            }else{
                y++;
            }
            mat[x][y] = -1;
        }
        /*
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                printf("%d ",mat[i][j]);
            }
            puts("");
        }
        puts("");*/
        n--;

    }

    return 0;
}
