#!/bin/sh

gcc -m32 -c run.s -o asm.o 
gcc -m32 -c main.c -o main.o
gcc -m32 asm.o main.o
./a.out
rm a.out *.o