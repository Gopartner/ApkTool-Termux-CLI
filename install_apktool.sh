#!/bin/bash

echo "🔹 Menginstal Apktool..."

# Unduh versi yang sesuai
APKTOOL_JAR="apktool_2.5.0.jar"
APKTOOL_URL="https://bitbucket.org/iBotPeaches/apktool/downloads/$APKTOOL_JAR"
INSTALL_DIR="/data/data/com.termux/files/usr/bin"
APKTOOL_BIN="$INSTALL_DIR/apktool"

# Pastikan folder bin ada
mkdir -p $INSTALL_DIR

# Download apktool jika belum ada
if [ ! -f "$INSTALL_DIR/$APKTOOL_JAR" ]; then
    echo "🔹 Mengunduh Apktool..."
    curl -L -o "$INSTALL_DIR/$APKTOOL_JAR" "$APKTOOL_URL"
else
    echo "✅ Apktool sudah ada, melewati unduhan."
fi

# Buat skrip wrapper
echo "🔹 Membuat skrip apktool di $APKTOOL_BIN"
cat > "$APKTOOL_BIN" << EOF
#!/bin/bash
exec java -jar "$INSTALL_DIR/$APKTOOL_JAR" "\$@"
EOF

chmod +x "$APKTOOL_BIN"

echo "✅ Instalasi selesai! Gunakan perintah 'apktool' untuk menjalankan."

