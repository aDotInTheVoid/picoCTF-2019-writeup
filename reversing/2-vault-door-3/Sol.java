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
