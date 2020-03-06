# vault-door-7
```java
    public int[] passwordToIntArray(String hex) {
        int[] x = new int[8];
        byte[] hexBytes = hex.getBytes();
        for (int i=0; i<8; i++) {
            x[i] = hexBytes[i*4]   << 24
                 | hexBytes[i*4+1] << 16
                 | hexBytes[i*4+2] << 8
                 | hexBytes[i*4+3];
        }
        return x;
    }

    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        int[] x = passwordToIntArray(password);
        return x[0] == 1096770097
            && x[1] == 1952395366
            && x[2] == 1600270708
            && x[3] == 1601398833
            && x[4] == 1716808014
            && x[5] == 1734293815
            && x[6] == 1667379558
            && x[7] == 859191138;
    }
```
We can reverse this with the [`p32`](https://docs.pwntools.com/en/stable/util/packing.html#pwnlib.util.packing.p32) packing function
```python
>>> from pwn import *
>>> l = [1096770097,1952395366,1600270708,1601398833,1716808014,1734293815,1667379558,859191138]
>>> b"".join(p32(i, endian='big') for i in l)
b'A_b1t_0f_b1t_sh1fTiNg_97cb1f367b'
```
Flag: `picoCTF{A_b1t_0f_b1t_sh1fTiNg_97cb1f367b}`