#include <stdio.h>

/*
* For any given two numbers n and m, you have to find n*m without using any multiplication operator.
*/


int multiply(int n, int m){  
    int ans = 0, count = 0;
    while (m)
    {
        // check for set bit and left 
        // shift n, count times
        if (m & 1){ 
        	ans += n << count;
		printf("%d\n",ans);
	}
 
        // increment of place value (count)
        count++;
        m = m >> 1;
    }
    return ans;
}
 
// Driver program 
int main()
{
    int n = 20 , m = 13;
    printf("\n%d\n",multiply(n, m));
    return 0;
}
