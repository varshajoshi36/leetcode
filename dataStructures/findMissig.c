#include<stdio.h>
 
int findMissing(int array[], int start, int end, int add_val) {
	if(start < end){
		int mid = (start + end)/2;
		if(array[mid] == (mid + add_val)){
			return findMissing(array, mid + 1, end, add_val);
		}else if(array[mid] > mid + add_val){
			return findMissing(array, start, mid, add_val);
		}
	}else{
		if(start + add_val != array[start])
			return start + add_val;
		else 
			return -1;
	}
}
 
// driver program to test above function
int main(){
	int arr[] = {1, 2, 4, 5, 6, 7, 8, 9};
	int n = sizeof(arr)/sizeof(arr[0]);
	printf("First missing element is %d\n",
	findMissing(arr, 0, n-1, arr[0]));
	return 0;
}
