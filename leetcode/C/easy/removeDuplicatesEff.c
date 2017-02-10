#include <stdio.h>

int main(){
	int arr[6] = {1,1,1,2,2,3};
	int newSize = removeDuplicates(arr, 6);
	printf("%d\n", newSize);
	return 0;
}

int removeDuplicates(int* nums, int numsSize) {
	int index;
	int lastElement = nums[numsSize - 1];
	int replaceAt;
	if(numsSize == 0)
		replaceAt = 0;
	else
		replaceAt = 1;
	for(index = 1; index < numsSize; index++){
		if(nums[index] == lastElement){
			returnSize = index + 1;
			break;
		}
		if(nums[index] > nums[index - 1]){
			nums[replaceAt++] = nums[index];
		}
	}
	return replaceAt + 1;
}
