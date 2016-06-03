#include <stdio.h>

#define GET_ARRAY_LEN(array,len){len=sizeof(array)/sizeof(array[0]);}

void print(int array[], int len){
    for (int i=0;i<len;i++) {
        printf("%d ", array[i]);
        if (i%4 == 3) {
            printf("\n");
        }
    }
    printf("\n");
}


int main(){
    int a[10];
    int i = 0;
    while (i<10){
        scanf("%d",&a[i]);
        i++;
    }
    // int a[] = {5,12,2,6,1,24,15,11,7,3};
    int len;
    GET_ARRAY_LEN(a,len);
    print(a,len);
    return 0;
}
