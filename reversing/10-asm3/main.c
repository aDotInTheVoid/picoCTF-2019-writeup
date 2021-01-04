#include <stdio.h>


int asm3(int a, int b, int c);

void main() {
    int result = asm3(0xd46c9935,0xdfe28722,0xb335450f);
    printf("0x%x\n", result);
}