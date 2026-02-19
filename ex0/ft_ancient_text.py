def ft_ancient_text():
    print("CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    file_path = 'ancient_fragment.txt'
    print(f"Accessing Storage Vault: {file_path}")
    try:
        f = open(file_path, "r")
        print("Connection established...")
        print("RECOVERED DATA:\n")
        print(f.read())
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        f.close()


if __name__ == '__main__':
    ft_ancient_text()