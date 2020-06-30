# droids3

Again decompile with `jadx three.apk -d three`

Looking at `FlagstaffHill`

```java
package com.hellocmu.picoctf;

import android.content.Context;

public class FlagstaffHill {
    public static native String cilantro(String str);

    public static String nope(String input) {
        return "don't wanna";
    }

    public static String yep(String input) {
        return cilantro(input);
    }

    public static String getFlag(String input, Context ctx) {
        return nope(input);
    }
}
```

We will use apktool to change the `nope` call to `yep`

```
apktool d three.apk 
```

Then in `three/smali/com/hellocmu/picoctf/FlagstaffHill.smali`, we can see the smali version of the method.

```smali
.method public static getFlag(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;
    .locals 1
    .param p0, "input"    # Ljava/lang/String;
    .param p1, "ctx"    # Landroid/content/Context;

    .line 19
    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->nope(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    .line 20
    .local v0, "flag":Ljava/lang/String;
    return-object v0
.end method
```

We can change the `invoke-static` to call `yep`

```smali
    invoke-static {p0}, Lcom/hellocmu/picoctf/FlagstaffHill;->yep(Ljava/lang/String;)Ljava/lang/String;
```

Then we build this change into a new apk

```
apktool b three -o three_run.apk
```

As we've modified it, we need to [sign it](https://stackoverflow.com/questions/10930331/how-to-sign-an-already-compiled-apk)

```
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore three_run.apk alias_name
```

Running the new APK, we get the flag

Flag: `picoCTF{tis.but.a.scratch}`