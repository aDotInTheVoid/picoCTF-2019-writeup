# vault-door-4
```java
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0142, 071 ,
            'e' , '9' , '2' , 'f' , '7' , '6' , 'a' , 'c' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
```
We can just convert the bytes to string and be done.
```java
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0142, 071 ,
            'e' , '9' , '2' , 'f' , '7' , '6' , 'a' , 'c' ,
        };
        String password = new String(myBytes);
        System.out.println(password);
```
Running gives `jU5t_4_bUnCh_0f_bYt3s_b9e92f76ac`

Flag: `picoCTF{jU5t_4_bUnCh_0f_bYt3s_b9e92f76ac}`