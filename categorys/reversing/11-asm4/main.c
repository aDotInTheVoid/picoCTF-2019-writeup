#include <stdio.h>

int asm4(void*);

void main() {
    int res = asm4("picoCTF_d7243");
    printf("0x%x\n", res);
}