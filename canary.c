#include <stdio.h>
void foo() {
    char buf[16];
    fgets(buf, sizeof(buf), stdin);
    printf(buf);
}
void bar() {
    char buf[16];
    scanf("%s", buf);
}
int main() {
    foo();
    bar();
}
