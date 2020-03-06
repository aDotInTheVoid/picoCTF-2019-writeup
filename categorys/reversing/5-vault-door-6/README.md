# vault-door-6
```java
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x67, 0x6d, 0x33, 0x34, 0x6c, 0x60, 0x33,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
```
This uses the `^` ([bitwise XOR](https://www.geeksforgeeks.org/bitwise-operators-in-java/)).

As the clue tells us `X ^ Y = Z` imply `Z ^ Y = X`. Therefor we can bitwise XOR the bytes with `0x55` to get the password.

```java
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x67, 0x6d, 0x33, 0x34, 0x6c, 0x60, 0x33,
        };
        byte[] password = new byte[32];
        for (int i=0; i<32; i++) {
            password[i] = (byte)(myBytes[i] ^ 0x55);
        }
        System.out.println(new String(password));
```
gives `n0t_mUcH_h4rD3r_tH4n_x0r_28fa95f`

Flag: `picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_28fa95f}`