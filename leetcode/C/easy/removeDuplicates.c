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
	int returnSize;
	if(numsSize == 0)
		returnSize = 0;
	else
		returnSize = numsSize;
	for(index = 0; index < numsSize - 1; index++){
		if(nums[index] == lastElement){
			returnSize = index + 1;
			break;
		}
		if (nums[index] == nums[index + 1]){
			if(index <= numsSize - 2){
				int index2;
				int replaceAt = index + 1;
				int nextIndex = index + 2;
				while(nextIndex < numsSize){
					if(nums[index] == nums[nextIndex])
						nextIndex += 1;
					else{
						nums[replaceAt] = nums[nextIndex];
						replaceAt += 1;
						nextIndex += 1;
					}
				}
			}
		}

	}
	return returnSize;
}
