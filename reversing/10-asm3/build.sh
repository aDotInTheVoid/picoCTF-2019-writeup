#!/bin/sh
gcc -m32 -c main.c -o main.o
gcc -m32 -c run.s -o asm.o
gcc -m32 main.o asm.o
./a.out
rm *.o a.out