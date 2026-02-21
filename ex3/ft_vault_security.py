def vault_security():
    """Safely reads and appends to a file"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    file_name = "classified_data.txt"
    try:
        with open(file_name, "r") as f:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            for line in f:
                print(line, end="")
            print("\n")
        print("SECURE PRESERVATION:")
        with open(file_name, "a") as f:
            f.write("\n[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
    except FileNotFoundError:
        print("Error detected. Check your file_name.")

    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == '__main__':
    vault_security()
