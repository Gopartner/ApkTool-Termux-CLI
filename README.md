<p align="center">
<a href="https://gopartner.github.io/"><img title="Made in INDONESIA" src="https://img.shields.io/badge/MADE%20IN-INDONESIA-SCRIPT?colorA=%23ff8100&colorB=%23017e40&colorC=%23ff0000&style=for-the-badge"></a>
</p>

<p align="center">
<a href="https://gopartner.github.io/"><img title="Tool" src="https://img.shields.io/badge/Tool-Apktool-green.svg?style=flat-square"></a>
<a href="https://gopartner.github.io/"><img title="Version" src="https://img.shields.io/badge/Version-2.6.1-green.svg?style=flat-square"></a>
<a href="https://gopartner.github.io/"><img title="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square"></a>
</p>

<p align="center">
<a href="https://github.com/yudibilly"><img title="Github" src="https://img.shields.io/badge/Yudibilly-brightgreen?style=for-the-badge&logo=github"></a>
<a href="https://youtube.com/@yudibilly"><img title="YouTube" src="https://img.shields.io/badge/YouTube-Yudibilly-red?style=for-the-badge&logo=Youtube"></a>
</p>


---

### **📌 Apktool-Termux-CLI**

✅ **Versi terbaru apktool 2.6.1 untuk Termux oleh Yudibilly**  
✅ **Versi: 2.6.1**  

---

### **📲 Tersedia di:**
✔️ Termux  

---

### **🛠️ Persyaratan:**
✔️ Java  

---

### **🔥 Fitur:**
✅ **Versi Apktool 2.6.1**  
✅ **Termasuk Java!**
✅ **Mudah digunakan untuk pemula!**  

---

## **📌 Instalasi di Termux:**
```bash
apt-get update -y
apt-get upgrade -y
git clone https://github.com/Gopartner/ApkTool-Termux-CLI.git
cd $HOME
ls
cd Apktool-Termux-CLI
chmod +x *
make
app.py (jalankan dengan make)
operasi.py (jalankan pada tab baru [ctrl+t])
```
## struktur project setelah install
```bash
~/ApkTool-Termux-CLI
├── Makefile
├── README.md
├── apks
│   └── base.apk
├── app.py
├── install_apktool.sh
├── operasi.py
├── output
└── uninstall_apktool.sh
```

<p align="center">
<a href="https://github.com/gopartner"><img title="GitHub" src="https://img.shields.io/badge/GitHub-GoPartner-brightgreen?style=for-the-badge&logo=github"></a>
<a href="https://www.instagram.com/yudibilly"><img title="Instagram" src="https://img.shields.io/badge/Instagram-Yudibilly-red?style=for-the-badge&logo=instagram"></a>

## Berikut adalah contoh sederhana untuk memahami tiga cara menampilkan konten di Android:

### 1.Nilai yang ditetapkan langsung di XML
contoh:
```bash
<!-- 1. Nilai yang ditetapkan langsung di XML -->
    <TextView
        android:id="@+id/textViewDirect"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Teks langsung di XML" />

```
### 2.Resource yang dideklarasikan dalam file resource
contoh:
```bash
<!-- 2. Resource yang dideklarasikan dalam file resource -->
    <TextView
        android:id="@+id/textViewResource"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/hello_resource" />

```
### 3.Data dinamis yang di-set melalui kode program saat aplikasi berjalan
contoh:
```bash
<!-- 3. Data dinamis yang di-set melalui kode program -->
    <TextView
        android:id="@+id/textViewDynamic"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />
```
## Langkah 1: Buat Layout XML (activity_main.xml)
<p>
Buat file layout di folder res/layout/activity_main.xml dengan isi seperti berikut:
</p>

```bash
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:padding="16dp"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <!-- 1. Nilai yang ditetapkan langsung di XML -->
    <TextView
        android:id="@+id/textViewDirect"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Teks langsung di XML" />

    <!-- 2. Resource yang dideklarasikan dalam file resource -->
    <TextView
        android:id="@+id/textViewResource"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/hello_resource" />

    <!-- 3. Data dinamis yang di-set melalui kode program -->
    <TextView
        android:id="@+id/textViewDynamic"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

</LinearLayout>
``` 
<p>
Pada contoh di atas:

textViewDirect memiliki teks yang ditulis langsung di atribut android:text.
textViewResource mengambil teks dari resource string yang didefinisikan.
textViewDynamic tidak memiliki teks awal, akan diisi secara dinamis melalui kode.
</p>

### Langkah 2: Deklarasikan String Resource (strings.xml)
<p>
Buka atau buat file res/values/strings.xml dan tambahkan string resource berikut:
</p>
    
```bash
<resources>
    <string name="app_name">LatihanTeks</string>
    <string name="hello_resource">Halo dari Resource</string>
</resources>
```
<p>
Penjelasan:

String dengan nama hello_resource akan dipakai oleh textViewResource melalui atribut android:text="@string/hello_resource".
</p>
### Langkah 3: Atur Data Dinamis di Kode Program (MainActivity.java atau MainActivity.kt)
<p>
Buat atau buka file Activity (misalnya, MainActivity.java) dan tambahkan kode untuk mengisi textViewDynamic secara dinamis.

Contoh dengan Java:
</p>
```bash
package com.example.latihanteks;

import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Ambil referensi ke textViewDynamic
        TextView textViewDynamic = findViewById(R.id.textViewDynamic);

        // 3. Set data dinamis (misalnya, data diambil dari API, database, atau perhitungan)
        String dynamicText = "Data dinamis yang di-set melalui kode program saat runtime";
        textViewDynamic.setText(dynamicText);
    }
}

```
<p>
Contoh dengan Kotlin:
</p>
```bash
package com.example.latihanteks

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_main.*  // Jika menggunakan synthetic, atau gunakan findViewById

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // 3. Set data dinamis
        textViewDynamic.text = "Data dinamis yang di-set melalui kode program saat runtime"
    }
}

```
<p>
Praktik dan Uji Coba
Nilai langsung di XML:

Jalankan aplikasi, dan lihat textViewDirect menampilkan teks yang sudah ditulis langsung di layout.
Resource yang dideklarasikan:

Lihat textViewResource yang menampilkan teks dari file strings.xml.
Data dinamis melalui kode:

textViewDynamic akan mendapatkan nilai yang di-set oleh kode di dalam onCreate().
Dengan contoh ini, Anda dapat memahami dan berlatih ketiga metode untuk menampilkan konten di Android. Anda juga bisa mencoba mengganti nilai-nilai tersebut atau menambahkan logika untuk mengambil data dari sumber lain (misalnya, API) untuk melatih pemahaman tentang data dinamis.

Apakah ada bagian lain yang ingin Anda eksplorasi atau pertanyaan terkait latihan ini?
</p>

#### ☕ Dukung Saya dengan belikan kopi

[![Saweria](https://img.shields.io/badge/💰%20Donasi%20di-Saweria-orange?style=for-the-badge&logo=buy-me-a-coffee)](https://saweria.co/yudibilly)



