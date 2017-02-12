#include <stdio.h>

/* Function to get no of set bits in binary
   representation of passed binary no. */
unsigned int countSetBits(unsigned int n){
	unsigned int count = 0;
	while(n){
		count += n & 1;
		n >>= 1;
	}
	return count;
}
 
/* Program to test function countSetBits */
int main(){
	int i = 19;
	printf("%d\n", countSetBits(i));
	return 0;
}
