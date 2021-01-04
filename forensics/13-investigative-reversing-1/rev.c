void main(void)

{
  FILE *flag_file;
  FILE *mistery;
  FILE *mistery2;
  FILE *mistery3;
  long in_FS_OFFSET;
  char flag3;
  int i1;
  int i2;
  int i3;
  char flag [4];
  char flag5;
  char flag6;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  flag_file = fopen("flag.txt","r");
  mistery = fopen("mystery.png","a");
  mistery2 = fopen("mystery2.png","a");
  mistery3 = fopen("mystery3.png","a");
  if (flag_file == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (mistery == (FILE *)0x0) {
    puts("mystery.png is missing, please run this on the server");
  }
  fread(flag,0x1a,1,flag_file);
  fputc((int)flag[1],mistery3);
  fputc((int)(char)(flag[0] + '\x15'),mistery2);
  fputc((int)flag[2],mistery3);
  flag3 = flag[3];
  fputc((int)flag6,mistery3);
  fputc((int)flag5,mistery);
  i1 = 6;
  while (i1 < 10) {
    flag3 = flag3 + '\x01';
    fputc((int)flag[(long)i1],mistery);
    i1 = i1 + 1;
  }
  fputc((int)flag3,mistery2);
  i2 = 10;
  while (i2 < 0xf) {
    fputc((int)flag[(long)i2],mistery3);
    i2 = i2 + 1;
  }
  i3 = 0xf;
  while (i3 < 0x1a) {
    fputc((int)flag[(long)i3],mistery);
    i3 = i3 + 1;
  }
  fclose(mistery);
  fclose(flag_file);
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}