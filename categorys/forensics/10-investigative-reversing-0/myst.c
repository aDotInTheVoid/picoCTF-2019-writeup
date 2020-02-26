void main(void)

{
  long lVar1;
  FILE *flag_file;
  FILE *png_file;
  size_t sucess;
  long in_FS_OFFSET;
  int i;
  int j;
  char flag4 [4];
  char flag5;
  char flag6;
  char local_29;
  
  lVar1 = *(long *)(in_FS_OFFSET + 0x28);
  flag_file = fopen("flag.txt","r");
  png_file = fopen("mystery.png","a");
  if (flag_file == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (png_file == (FILE *)0x0) {
    puts("mystery.png is missing, please run this on the server");
  }
  sucess = fread(flag4,0x1a,1,flag_file);
  if ((int)sucess < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("at insert");
  fputc((int)flag4[0],png_file);
  fputc((int)flag4[1],png_file);
  fputc((int)flag4[2],png_file);
  fputc((int)flag4[3],png_file);
  fputc((int)flag5,png_file);
  fputc((int)flag6,png_file);
  i = 6;
  while (i < 0xf) {
    fputc((int)(char)(flag4[(long)i] + '\x05'),png_file);
    i = i + 1;
  }
  fputc((int)(char)(local_29 + -3),png_file);
  j = 0x10;
  while (j < 0x1a) {
    fputc((int)flag4[(long)j],png_file);
    j = j + 1;
  }
  fclose(png_file);
  fclose(flag_file);
  if (lVar1 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}