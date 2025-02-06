# Makefile untuk instalasi, uninstall, dan menjalankan aplikasi modifikasi APK

# Variabel
PYTHON=python
INSTALL_SCRIPT=install_apktool.sh
UNINSTALL_SCRIPT=uninstall_apktool.sh
APP_SCRIPT=app.py

.PHONY: all install uninstall run clean menu

# Jika pengguna hanya menjalankan 'make', tampilkan menu
all: menu

menu:
	@echo ""
	@echo "🔹 PILIHAN MENU 🔹"
	@echo "1) Install Apktool"
	@echo "2) Uninstall Apktool"
	@echo "3) Jalankan Aplikasi Modifikasi APK"
	@echo "4) Bersihkan File Sementara"
	@echo "5) Keluar"
	@echo ""
	@read -p "Masukkan pilihan [1-5]: " pilihan; \
	case $$pilihan in \
		1) make install ;; \
		2) make uninstall ;; \
		3) make run ;; \
		4) make clean ;; \
		5) echo "Keluar..."; exit 0 ;; \
		*) echo "Pilihan tidak valid!" ;; \
	esac

# Instalasi Apktool
install:
	@echo "🔹 Menginstal Apktool..."
	@bash $(INSTALL_SCRIPT)
	@echo "✅ Instalasi selesai!"

# Uninstall Apktool
uninstall:
	@echo "🔹 Menghapus Apktool..."
	@bash $(UNINSTALL_SCRIPT)
	@echo "✅ Apktool telah dihapus!"

# Menjalankan aplikasi
run:
	@echo "🔹 Menjalankan aplikasi modifikasi APK..."
	@$(PYTHON) $(APP_SCRIPT)

# Membersihkan file temporary (jika ada)
clean:
	@echo "🔹 Membersihkan file sementara..."
	@rm -rf *.pyc __pycache__
	@echo "✅ Pembersihan selesai!"

