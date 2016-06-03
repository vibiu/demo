#include <stdio.h>
#include <string.h>

#define STR_LEN 30
char *myStrcpy(char *strDest, const char *strSrc){
    if(strDest == NULL || strSrc == NULL)
        return NULL;
    
    if(strDest == strSrc)
        return strDest;
    char *tempptr = strDest ;
    while( (*strDest++ = *strSrc++) != '\0');
        return tempptr ;
}

int main( void ){
    char input[STR_LEN];
    char strDest[STR_LEN];
    char *strSrc = input;

    fgets(input,STR_LEN,stdin);
    memset(strDest,0 , STR_LEN);
    
    printf("strDest = %s\n", strDest);
    myStrcpy(strDest, strSrc);
    printf("strDest = %s\n", strDest);
    return 0;
}
