import os

def final_clean_up():
    print("🧹 [CLEANER] Menghapus Log Percobaan & File Sampah Digital...")
    # Menghapus file sementara (.tmp, .log lama)
    extensions_to_clean = ['.tmp', '.log', '.bak']
    for root, dirs, files in os.walk("."):
        for file in files:
            if any(file.endswith(ext) for ext in extensions_to_clean):
                os.remove(os.path.join(root, file))
                print(f"🗑️ Deleted: {file}")
    
    print("✨ [STATUS] Repositori $QSTATE Murni & Siap Tempur.")

if __name__ == "__main__":
    final_clean_up()
