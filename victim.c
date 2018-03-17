// victim.c
# include <stdio.h>
int foo() {
    char buf[10];
    scanf("%s", buf);
    printf("hello %s\n", buf);
    return 0;
}
int main() {
    foo();
    printf("good bye!\n");
    return 0;
}
void dummy()
{
    __asm__("nop; jmp esp");
} 
