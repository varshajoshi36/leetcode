#include <stdio.h>
#include <string.h>

int main(){
	char version1[] = "2.0.27";
	char version2[] = "1.0.32";
	printf("%s\n%s\n", version1, version2);
	int greater = greaterVersion(version1, version2);
	if(greater == 1)
		printf("version 1 is latest\n");
	else if(greater == 2)
		printf("version 2 is latest\n");
	else
		printf("Both are equal\n");
	return 0;
}

int greaterVersion(char* vers1, char* vers2){
	int len1 = strlen(vers1);
	int len2 = strlen(vers2);
	
	int vnum1, vnum2;
	int ind1, ind2;
	for(ind1 = 0, ind2 = 0; (ind1 < len1 || ind2 < len2); ){
		vnum1 = 0;
		vnum2 = 0;
		while(ind1 < len1 && vers1[ind1] != '.'){
			vnum1 = vnum1 * 10 + (vers1[ind1] - '0');
			ind1++;
		}
		while(ind2 < len2 && vers2[ind2] != '.'){
			vnum2 = vnum2 * 10 + (vers2[ind2] - '0');
			ind2++;
		}

		if(vnum1 > vnum2)
			return 1;

		if(vnum2 > vnum1)
			return 2;

		ind1++;
		ind2++;
	}
	return 0;
}


