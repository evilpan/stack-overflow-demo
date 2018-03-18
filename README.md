# Stack Overflow Demo

[栈溢出漏洞的利用和缓解][blog]中所使用到的代码和exploit.

## Build victims:
    
    make

## Tips:

### common

spawn a new shell that disable ASLR:

    setarch `uname -m` -R /bin/bash

print load address of shared objects:

    LD_TRACE_LOADED_OBJECTS=1 /bin/ls

print ELF headers:

    readelf -h /bin/ls

print symbols:

    readelf -s /lib/i386-linux-gnu/libc.so.6
    rabin2 -s /lib/i386-linux-gnu/libc.so.6
    nm -D /lib/i386-linux-gnu/libc.so.6

### radare2

do some math:

    rax2 =16 0xf7752000+0x8888*2

characters to hex string:

    rax2 -S helloworld

generate De Brujin Sequence:

    ragg2 -P 40 -r

assembly:

    rasm2 -a x86 -b 32 "jmp esp"

disassembly:

    rasm2 -a x86 -b 32 -d "ffe4"

find string in binary:

    rafind2 -s "/bin/sh" /lib/i386-linux-gnu/libc.so.6


[blog]:#
