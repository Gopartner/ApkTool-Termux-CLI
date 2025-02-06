import os
import re
import sys
import time
import curses
from colorama import Fore, Style, init

init(autoreset=True)  # Inisialisasi colorama agar warna otomatis reset setelah dipakai

# Fungsi untuk menampilkan animasi loading
def loading_animation(message, duration=3):
    for _ in range(duration):
        for dots in range(4):  # Animasi titik (0-3 titik)
            sys.stdout.write(f"\r{message}{'.' * dots}   ")
            sys.stdout.flush()
            time.sleep(0.5)
    print("\r" + " " * len(message) + "   ", end="\r")  # Hapus animasi setelah selesai

# Fungsi untuk menampilkan menu navigasi folder di terminal
def list_folders(base_path):
    return [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]

def menu(stdscr, folders):
    curses.curs_set(0)  # Sembunyikan kursor
    stdscr.clear()
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Pilih folder hasil decompile (gunakan ↑/↓ dan Enter):", curses.A_BOLD)

        for idx, folder in enumerate(folders):
            if idx == current_row:
                stdscr.addstr(idx + 2, 2, f"> {folder}", curses.A_REVERSE)  # Highlight pilihan
            else:
                stdscr.addstr(idx + 2, 2, f"  {folder}")

        stdscr.refresh()
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(folders) - 1:
            current_row += 1
        elif key == 10:  # Enter
            return folders[current_row]

# Fungsi untuk menganalisis struktur APK
def analyze_apk_structure(base_path):
    print(f"\n{Fore.CYAN}[INFO] Menganalisis struktur APK...{Style.RESET_ALL}")
    loading_animation("Menganalisis struktur APK")

    structure = {
        "AndroidManifest": None,
        "Smali_Files": [],
        "Layout_XML": [],
        "Important_Configs": [],
    }

    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            if file == "AndroidManifest.xml":
                structure["AndroidManifest"] = file_path
            
            elif file.endswith(".xml") and "res/layout" in root:
                structure["Layout_XML"].append(file_path)
            
            elif file.endswith(".smali"):
                structure["Smali_Files"].append(file_path)
            
            elif file in ["apktool.yml", "proguard-project.txt"]:
                structure["Important_Configs"].append(file_path)

    return structure

# Fungsi untuk menemukan method dalam file Smali
def find_smali_methods(smali_file):
    methods = []
    with open(smali_file, "r", encoding="utf-8") as file:
        for line in file:
            match = re.search(r"\.method (public|private|protected) (.*)\(", line)
            if match:
                methods.append(match.group(2))
    return methods

# Fungsi untuk menganalisis Smali yang berhubungan dengan UI
def analyze_smali_code(smali_files):
    print(f"\n{Fore.CYAN}[INFO] Menganalisis file Smali...{Style.RESET_ALL}")
    loading_animation("Menganalisis Smali")

    ui_related_methods = {}
    keywords = ["setContentView", "onClick", "startActivity"]

    total_files = len(smali_files)
    for idx, smali_file in enumerate(smali_files):
        # Menampilkan progres
        sys.stdout.write(f"\r{Fore.YELLOW}[PROGRESS] Memeriksa Smali {idx+1}/{total_files}...{Style.RESET_ALL} ")
        sys.stdout.flush()

        methods = find_smali_methods(smali_file)
        
        for method in methods:
            for keyword in keywords:
                if keyword in method:
                    if smali_file not in ui_related_methods:
                        ui_related_methods[smali_file] = []
                    ui_related_methods[smali_file].append(method)
    
    print(f"\n{Fore.GREEN}[SUKSES] Analisis Smali selesai!{Style.RESET_ALL}")
    return ui_related_methods

# Fungsi untuk menampilkan hasil analisis dengan warna
def print_colored_output(structure, smali_analysis):
    print(f"\n{Fore.CYAN}=== APK Structure Analysis ==={Style.RESET_ALL}")

    # AndroidManifest.xml
    if structure["AndroidManifest"]:
        print(f"\n{Fore.GREEN}[+] AndroidManifest.xml ditemukan:{Style.RESET_ALL} {structure['AndroidManifest']}")
    else:
        print(f"\n{Fore.RED}[-] AndroidManifest.xml tidak ditemukan.{Style.RESET_ALL}")

    # Layout XML Files
    print(f"\n{Fore.GREEN}[+] Layout XML Files:{Style.RESET_ALL}")
    for xml in structure["Layout_XML"]:
        print(f"    {Fore.YELLOW}- {xml}{Style.RESET_ALL}")

    # Smali Files
    print(f"\n{Fore.GREEN}[+] Smali Files:{Style.RESET_ALL}")
    for smali in structure["Smali_Files"][:10]:  # Batasi tampilan ke 10 file pertama
        print(f"    {Fore.MAGENTA}- {smali}{Style.RESET_ALL}")

    # Konfigurasi Penting
    print(f"\n{Fore.GREEN}[+] Konfigurasi Penting:{Style.RESET_ALL}")
    for config in structure["Important_Configs"]:
        print(f"    {Fore.BLUE}- {config}{Style.RESET_ALL}")

    # Analisis Smali
    print(f"\n{Fore.CYAN}=== SMALI ANALYSIS ==={Style.RESET_ALL}")
    for file, methods in smali_analysis.items():
        print(f"\n{Fore.GREEN}[+] {file}{Style.RESET_ALL}")
        for method in methods:
            print(f"    {Fore.YELLOW}- {method}{Style.RESET_ALL}")

    # Rekomendasi Edit
    print(f"\n{Fore.CYAN}=== REKOMENDASI EDIT ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}- Edit {Fore.BLUE}AndroidManifest.xml{Fore.YELLOW} untuk menambah izin atau Activity baru.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}- Edit {Fore.BLUE}res/layout/*.xml{Fore.YELLOW} untuk mengubah tampilan atau menambah modal.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}- Edit file {Fore.MAGENTA}.smali{Fore.YELLOW} yang mengandung {Fore.CYAN}setContentView, onClick, startActivity{Fore.YELLOW} untuk menambah logika.{Style.RESET_ALL}")

# Fungsi utama
def main():
    base_path = "output/"
    
    if not os.path.exists(base_path):
        print(f"{Fore.RED}[ERROR] Folder 'output/' tidak ditemukan!{Style.RESET_ALL}")
        return

    folders = list_folders(base_path)
    
    if not folders:
        print(f"{Fore.RED}[ERROR] Tidak ada folder dalam 'output/'.{Style.RESET_ALL}")
        return

    selected_folder = curses.wrapper(menu, folders)
    
    print(f"\n{Fore.GREEN}Anda memilih: {selected_folder}{Style.RESET_ALL}")
    selected_path = os.path.join(base_path, selected_folder)
    print(f"{Fore.BLUE}Path lengkap: {selected_path}{Style.RESET_ALL}")

    # Jalankan analisis setelah memilih folder
    structure = analyze_apk_structure(selected_path)
    smali_analysis = analyze_smali_code(structure["Smali_Files"])
    
    print_colored_output(structure, smali_analysis)

if __name__ == "__main__":
    main()

