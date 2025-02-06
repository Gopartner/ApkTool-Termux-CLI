import os
import subprocess

APK_DIR = "apks"
OUTPUT_DIR = "output"

def list_apks():
    """Menampilkan daftar APK yang tersedia untuk didecompile."""
    apks = [f for f in os.listdir(APK_DIR) if f.endswith(".apk")]
    
    if not apks:
        print(f"Tidak ada file APK di folder {APK_DIR}. Silakan tambahkan file APK untuk dimodifikasi.")
        return None

    print("\n🔹 Pilih APK untuk dimodifikasi:")
    for i, apk in enumerate(apks, start=1):
        print(f"{i}) {apk}")
    
    try:
        choice = int(input("Masukkan nomor APK: ")) - 1
        if 0 <= choice < len(apks):
            return apks[choice]
    except ValueError:
        pass

    print("❌ Pilihan tidak valid!")
    return None

def decompile_apk(apk_file, output_name):
    """Mendekompilasi APK menggunakan apktool."""
    output_path = os.path.join(OUTPUT_DIR, output_name)
    
    print(f"\n⏳ Mendekompilasi {apk_file} ke folder {output_name}...")
    
    result = subprocess.run(
        ["apktool", "d", "-f", "-o", output_path, os.path.join(APK_DIR, apk_file)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    print(result.stdout)
    
    if os.path.exists(output_path) and os.listdir(output_path):
        print(f"✅ Decompile selesai: {output_path}\n")
        return output_path
    else:
        print(f"❌ Gagal mendekompilasi {apk_file}. Error:\n{result.stderr}")
        return None

def list_files(folder):
    """Menampilkan isi folder hasil decompile."""
    print("\n📂 Isi folder hasil decompile:")
    for root, dirs, files in os.walk(folder):
        level = root.replace(folder, "").count(os.sep)
        indent = " " * (level * 2)
        print(f"{indent}📂 {os.path.basename(root)}")
        subindent = " " * ((level + 1) * 2)
        for f in files:
            print(f"{subindent}📄 {f}")

def edit_file(folder):
    """Memilih file untuk diedit."""
    while True:
        list_files(folder)
        file_path = input("\nMasukkan nama file yang ingin diedit (atau ketik 'q' untuk kembali): ").strip()
        if file_path.lower() == 'q':
            break

        full_path = os.path.join(folder, file_path)
        if os.path.exists(full_path):
            subprocess.run(["nano", full_path])  # Ganti dengan editor yang tersedia di Termux
        else:
            print("❌ File tidak ditemukan!")

def main():
    """Menu utama untuk memilih APK dan operasi modifikasi."""
    os.makedirs(APK_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    apk_file = list_apks()
    if not apk_file:
        return

    output_name = input("\nMasukkan nama folder hasil decompile: ").strip()
    output_folder = decompile_apk(apk_file, output_name)
    if not output_folder:
        return

    while True:
        print("\n🔹 Pilih operasi:")
        print("1) Edit file tertentu")
        print("2) Tambah fitur/UI")
        print("3) Recompile APK")
        print("4) Sign APK")
        print("5) Keluar")

        choice = input("Masukkan pilihan: ").strip()

        if choice == "1":
            edit_file(output_folder)
        elif choice == "2":
            print("\n🛠️ Tambah fitur atau UI (belum diimplementasikan)")
        elif choice == "3":
            print("\n⏳ Merekompilasi APK...")
            subprocess.run(["apktool", "b", output_folder], shell=True)
        elif choice == "4":
            print("\n🔏 Menandatangani APK... (belum diimplementasikan)")
        elif choice == "5":
            break
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()

