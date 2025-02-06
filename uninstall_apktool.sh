#!/bin/bash

echo "🔹 Menghapus Apktool..."

INSTALL_DIR="/data/data/com.termux/files/usr/bin"
APKTOOL_JAR="$INSTALL_DIR/apktool_2.5.0.jar"
APKTOOL_BIN="$INSTALL_DIR/apktool"

# Hapus file
rm -f "$APKTOOL_JAR"
rm -f "$APKTOOL_BIN"

echo "✅ Apktool telah dihapus!"

