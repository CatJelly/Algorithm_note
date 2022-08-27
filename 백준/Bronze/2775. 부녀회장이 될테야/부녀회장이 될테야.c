#include <stdio.h>

#define size 15

int main(){
	int T, i, j;
    int k, n;
    
    int apt[size][size] = {0, };
    
    for( j=0 ; j<size ; j++ )
    	apt[0][j] = j;
    for( i=0 ; i<size ; i++ )
    	apt[i][1] = 1;
    
    for( i=1 ; i<size ; i++ )
    	for( j=2 ; j<size ; j++ )
        	apt[i][j] = apt[i-1][j] + apt[i][j-1];
    
    scanf("%d", &T);
    
    for( i=0 ; i<T ; i++ ){
    	scanf("%d", &k);
        scanf("%d", &n);
        
        printf("%d\n", apt[k][n]);
    }
    
	return 0;
}