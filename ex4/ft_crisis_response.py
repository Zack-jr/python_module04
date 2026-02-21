def crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        print("RESPONSE:  Archive not found in  storage matrix")
    finally:
        print("STATUS: Crisis handled, system stable")

    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt", "w") as f:
            f.read()
    except PermissionError:
        print("Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained")
    
    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", "r") as f:
            text = f.read()
        print(f"SUCCESS: Archive recovered - ``{text}''")
    except FileNotFoundError, PermissionError:
        

if __name__ == '__main__':
    crisis_response()