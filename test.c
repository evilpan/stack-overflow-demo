#include <stdio.h>
#include <stdlib.h>
void run(const char *file) {
    char shellcode[1000] = {0};
    FILE *fp = fopen(file, "r");
    size_t len = fread(shellcode, 1, 100, fp);
    printf("read %zu bytes shellcode\n", len);
    fclose(fp);
    (* (int(*)()) shellcode)();
}

int main(int argc, char *argv[]) {
    printf("system is at %p\n", system);
    if (argc != 2) {
        printf("Usage: %s /path/to/shellocde\n", argv[0]);
        return 1;
    }
    run(argv[1]);
}
