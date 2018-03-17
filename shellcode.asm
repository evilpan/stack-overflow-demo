; shellcode.asm
; see /usr/include/asm/unistd_32.h
mov eax, 1;
mov ebx, 66;
int 0x80;
