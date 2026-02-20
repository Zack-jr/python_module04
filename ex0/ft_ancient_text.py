def ft_ancient_text():
    """recovers data from a .txt file"""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    file_path = 'ancient_fragment.txt'
    print(f"Accessing Storage Vault: {file_path} \U0001F50D")
    try:
        f = open(file_path, "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        for line in f:
            print(f"🗃️ {line}", end="")
        f.close()
        print("\n\n🎉 Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("❌ ERROR: Storage vault not found. Run data generator first.")


if __name__ == '__main__':
    ft_ancient_text()
