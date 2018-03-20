# Stack Overflow Demo

[栈溢出漏洞的利用和缓解][blog]中所使用到的代码和exploit.

## 编译victim:
    
    make

## 小tips:

### 通用

新建一个禁用ASLR的shell:

    setarch `uname -m` -R /bin/bash

查看动态链接库准确的加载基址:

    LD_TRACE_LOADED_OBJECTS=1 /bin/ls

查看ELF头:

    readelf -h /bin/ls

查看符号:

    readelf -s /lib/i386-linux-gnu/libc.so.6
    rabin2 -s /lib/i386-linux-gnu/libc.so.6
    nm -D /lib/i386-linux-gnu/libc.so.6

### radare2

数学运算:

    rax2 =16 0xf7752000+0x8888*2

字符串转十六进制:

    rax2 -S helloworld

生成De Brujin序列:

    ragg2 -P 40 -r

汇编:

    rasm2 -a x86 -b 32 "jmp esp"

反汇编:

    rasm2 -a x86 -b 32 -d "ffe4"

在二进制文件中查找字符串:

    rafind2 -s "/bin/sh" /lib/i386-linux-gnu/libc.so.6


[blog]:https://www.pppan.net/blog/detail/2018-03-17-exploit-the-stack
