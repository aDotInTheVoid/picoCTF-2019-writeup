# Need For Speed

Again we use ghidra

```c
undefined8 main(void)

{
  header();
  set_timer();
  get_key();
  print_flag();
  return 0;
}
```

Here we call [`alarm`](https://man7.org/linux/man-pages/man2/alarm.2.html), so we have 1 sec untill we get the signal

However, we can actualy [ignore `SIGALRM`](https://stackoverflow.com/questions/26145952/gdb-sigalrm-alarm-clock-termination), like this 

```
$ gdb need-for-speed -quiet
Reading symbols from need-for-speed...
(No debugging symbols found in need-for-speed)
(gdb)  handle SIGALRM ignore
Signal        Stop	Print	Pass to program	Description
SIGALRM       No	No	No		Alarm clock
(gdb) run
Starting program: /tmp/need-for-speed
Missing separate debuginfos, use: dnf debuginfo-install glibc-2.31-2.fc32.x86_64
Keep this thing over 50 mph!
============================

Creating key...
Finished
Printing flag:
PICOCTF{Good job keeping bus #236cb1c9 speeding along!}
[Inferior 1 (process 63289) exited normally]
(gdb) quit
```