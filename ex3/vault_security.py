def vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("Initiating secure vault access...")
    file_name = "classified_data.txt"
    with open(file_name) as f:
        for line in f:
            print(line)

if __name__ == '__main__':
    vault_security()