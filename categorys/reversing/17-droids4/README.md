# droids4
```
jadx four.apk -d four
```

Again looking at `FlagstaffHill`

```java
package com.hellocmu.picoctf;
import android.content.Context;

public class FlagstaffHill {
    public static native String cardamom(String str);

    public static String getFlag(String input, Context ctx) {
        StringBuilder ace = new StringBuilder("aaa");
        StringBuilder jack = new StringBuilder("aaa");
        StringBuilder queen = new StringBuilder("aaa");
        StringBuilder king = new StringBuilder("aaa");
        ace.setCharAt(0, (char) (ace.charAt(0) + 4));
        ace.setCharAt(1, (char) (ace.charAt(1) + 19));
        ace.setCharAt(2, (char) (ace.charAt(2) + 18));
        jack.setCharAt(0, (char) (jack.charAt(0) + 7));
        jack.setCharAt(1, (char) (jack.charAt(1) + 0));
        jack.setCharAt(2, (char) (jack.charAt(2) + 1));
        queen.setCharAt(0, (char) (queen.charAt(0) + 0));
        queen.setCharAt(1, (char) (queen.charAt(1) + 11));
        queen.setCharAt(2, (char) (queen.charAt(2) + 15));
        king.setCharAt(0, (char) (king.charAt(0) + 14));
        king.setCharAt(1, (char) (king.charAt(1) + 20));
        king.setCharAt(2, (char) (king.charAt(2) + 15));
        if (input.equals("".concat(queen.toString()).concat(jack.toString()).concat(ace.toString()).concat(king.toString()))) {
            return "call it";
        }
        return "NOPE";
    }
}
```

What we want this to be is

```java
package com.hellocmu.picoctf;
import android.content.Context;

public class FlagstaffHill {
    public static native String cardamom(String str);

    public static String getFlag(String input, Context ctx) {
        StringBuilder ace = new StringBuilder("aaa");
        StringBuilder jack = new StringBuilder("aaa");
        StringBuilder queen = new StringBuilder("aaa");
        StringBuilder king = new StringBuilder("aaa");
        ace.setCharAt(0, (char) (ace.charAt(0) + 4));
        ace.setCharAt(1, (char) (ace.charAt(1) + 19));
        ace.setCharAt(2, (char) (ace.charAt(2) + 18));
        jack.setCharAt(0, (char) (jack.charAt(0) + 7));
        jack.setCharAt(1, (char) (jack.charAt(1) + 0));
        jack.setCharAt(2, (char) (jack.charAt(2) + 1));
        queen.setCharAt(0, (char) (queen.charAt(0) + 0));
        queen.setCharAt(1, (char) (queen.charAt(1) + 11));
        queen.setCharAt(2, (char) (queen.charAt(2) + 15));
        king.setCharAt(0, (char) (king.charAt(0) + 14));
        king.setCharAt(1, (char) (king.charAt(1) + 20));
        king.setCharAt(2, (char) (king.charAt(2) + 15));
        return cardamom("".concat(queen.toString()).concat(jack.toString()).concat(ace.toString()).concat(king.toString()))
    }
}
```

However, it's much easyer to edit the smali, than java, so we want to convert this 
[to java](https://stackoverflow.com/questions/29051781/convert-java-file-to-smali-file)

First we need some minor modification, so it can be compiled outside of android.

```java
public class FlagstaffHill {
    private class Context{}

    public static native String cardamom(String str);

    public static String getFlag(String input, Context ctx) {
        StringBuilder ace = new StringBuilder("aaa");
        StringBuilder jack = new StringBuilder("aaa");
        StringBuilder queen = new StringBuilder("aaa");
        StringBuilder king = new StringBuilder("aaa");
        ace.setCharAt(0, (char) (ace.charAt(0) + 4));
        ace.setCharAt(1, (char) (ace.charAt(1) + 19));
        ace.setCharAt(2, (char) (ace.charAt(2) + 18));
        jack.setCharAt(0, (char) (jack.charAt(0) + 7));
        jack.setCharAt(1, (char) (jack.charAt(1) + 0));
        jack.setCharAt(2, (char) (jack.charAt(2) + 1));
        queen.setCharAt(0, (char) (queen.charAt(0) + 0));
        queen.setCharAt(1, (char) (queen.charAt(1) + 11));
        queen.setCharAt(2, (char) (queen.charAt(2) + 15));
        king.setCharAt(0, (char) (king.charAt(0) + 14));
        king.setCharAt(1, (char) (king.charAt(1) + 20));
        king.setCharAt(2, (char) (king.charAt(2) + 15));
        return cardamom("".concat(queen.toString()).concat(jack.toString()).concat(ace.toString()).concat(king.toString()));
    }
}
```

```
/Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home/bin/javac FlagstaffHill.java
~/Library/Android/sdk/build-tools/30.0.0/dx --dex --output=d.dex FlagstaffHill.class
baksmali d d.dex 
```
Finaly we have the smali we need. Next we disaseble the apk.

```
apktool d four.apk
```
The go into `FlagstaffHill.smali`. And the end it looks like this (wo anotations)

```smali
# Finish generating the password
invoke-virtual {v4, v5}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    # Put it in v4
    move-result-object v4

    .line 36
    .local v4, "password":Ljava/lang/String;
    # Compare the input (p0, to the password)
    invoke-virtual {p0, v4}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    # Store in v5
    move-result v5

    # If not equal, goto :cond_0
    if-eqz v5, :cond_0

    # Create tht string "call it"
    const-string v5, "call it"

    # Return that string
    return-object v5

    # If passowrd was wrong, crate and return "NOPE"
    .line 37
    :cond_0
    const-string v5, "NOPE"

    return-object v5
.end method
```

The replace ment is this

```smali

    # Finish password generation
    invoke-virtual {v4, v5}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    # Store passord in v5
    move-result-object v4

    # Call cardamom with password
    invoke-static {v4}, Lcom/hellocmu/picoctf/FlagstaffHill;->cardamom(Ljava/lang/String;)Ljava/lang/String;

    # Store in v5
    move-result-object v5

    # Return v5
    return-object v5

.end method
```

Finaly rebuild the apk, and sign with the key

```
apktool b four -o four_run.apk
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000 
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore four_run.apk alias_name 
```

Running gives the flag.

Flag: `picoCTF{not.particularly.silly}`