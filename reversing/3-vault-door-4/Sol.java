import java.util.*;

class Sol{
    public static void main(String args[]){
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0142, 071 ,
            'e' , '9' , '2' , 'f' , '7' , '6' , 'a' , 'c' ,
        };
        String password = new String(myBytes);
        System.out.println(password);
    }
}