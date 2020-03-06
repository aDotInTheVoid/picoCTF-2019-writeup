# vault-door-1

```java
import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
	String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
	}
    }

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '7' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '3' &&
               password.charAt(30) == 'a' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == 'b' &&
               password.charAt(26) == '0' &&
               password.charAt(31) == '0';
    }
}
```
While brute force is easy, it's nicer to sort it. Using something like [vscode's box select](https://code.visualstudio.com/docs/editor/codebasics#_column-box-selection), take the relevent portion of the java.

```text
0)  == 'd
29) == '7
4)  == 'r
2)  == '5
23) == 'r
3)  == 'c
17) == '4
1)  == '3
7)  == 'b
10) == '_
5)  == '4
9)  == '3
11) == 't
15) == 'c
8)  == 'l
12) == 'H
20) == 'c
14) == '_
6)  == 'm
24) == '5
18) == 'r
13) == '3
19) == '4
21) == 'T
16) == 'H
27) == '3
30) == 'a
25) == '_
22) == '3
28) == 'b
26) == '0
31) == '0
```

Then you can pipe this into `sort --numeric-sort` to get:
```
0)  == 'd
1)  == '3
2)  == '5
3)  == 'c
4)  == 'r
5)  == '4
6)  == 'm
7)  == 'b
8)  == 'l
9)  == '3
10) == '_
11) == 't
12) == 'H
13) == '3
14) == '_
15) == 'c
16) == 'H
17) == '4
18) == 'r
19) == '4
20) == 'c
21) == 'T
22) == '3
23) == 'r
24) == '5
25) == '_
26) == '0
27) == '3
28) == 'b
29) == '7
30) == 'a
31) == '0
```
A simple script or [multicursor](https://code.visualstudio.com/docs/editor/codebasics#_multiple-selections-multicursor) will let you join the  last charecters.

`d35cr4mbl3_tH3_cH4r4cT3r5_03b7a0`. Flag: `picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_03b7a0}`