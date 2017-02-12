#include <stdio.h>

char* findTwoscomplement(char* str){
	int n = strlen(str);

	int i;
	for (i = n ; i >= 0 ; i--)
		if (str[i] == '1')
		    break;

	if (i == 0)
		return '1' + str;
	int k;
	for (k = i-1 ; k >= 0; k--){
		if (str[k] == '1')
		    str[k] = '0';
		else
		    str[k] = '1';
	}

	return str;
}

int main(){
	char str[] = "00000101";
	char twosCompl[] = findTwoscomplement(str);
	int i = 0;
	while(twosCompl[i] != '\0'){
		printf("%c",twosCompl[i]);
		i++;
	}
	printf("\n");
}
