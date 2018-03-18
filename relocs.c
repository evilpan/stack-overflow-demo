#include<stdio.h>
int main() {
    char buf[16];
    fscanf(stdin, "%s", buf);
    printf("input is %s\n", buf);
}
