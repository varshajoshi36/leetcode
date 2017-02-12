/**
 * (1) Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's 
 * in their binary representation and return them as an array.
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize) {

    int i = 0;
    int counter = 0;

    *returnSize += 1;
    int *count = (int*) malloc((*returnSize) * sizeof(int));
    
    count[0] = 0;
    
    for(i = 1; i <= num; i++) {
        count[i] = count[i & (i-1)] + 1;       
    }
    
    return count;
}

int main(){
	int *size = 19;
	int* arr = countBits(19, size);
	int i;
	for(i = 0; i <= *size; i++)
		;//printf("%d\t", arr[i]);
}
