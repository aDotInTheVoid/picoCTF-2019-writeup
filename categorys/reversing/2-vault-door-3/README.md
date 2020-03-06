# vault-door-3

Looking at the code, the important method is:
```java
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm16g84c_u_4_m0r846");
    }
```
Some basic reversing to move the other way gives
```java
import java.util.*;

class Sol {
    public static void main(String args[]) {
        char[] buffer = "jU5t_a_sna_3lpm16g84c_u_4_m0r846".toCharArray();
        char[] password = new char[100];
        int i;
        for (i=0; i<8; i++) {
            password[i] = buffer[i];
        }
        for (; i<16; i++) {
            password[23-i]=buffer[i];
        }
        for (; i<32; i+=2) {
            password[46-i]=buffer[i];
        }
        for (i=31; i>=17; i-=2) {
            password[i]=buffer[i];
        }
        String s = new String(password);
        System.out.println(s);
    }
}
```

Then we can compile and run with `javac Sol.java && java Sol` giving `jU5t_a_s1mpl3_an4gr4m_4_u_c08866`

Flag: `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c08866}`