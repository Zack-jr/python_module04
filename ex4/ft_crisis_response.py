def handle_crisis(file_name, crisis_type):
    """manages errors in during file manipulations"""

    if (crisis_type == "archive_not_found"):
        try:
            print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
            with open(file_name, "r") as f:
                f.read()
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
        finally:
            print("STATUS: Crisis handled, system stable\n")

    if (crisis_type == "denied_access"):
        try:
            print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
            with open(file_name, "r") as f:
                f.read()
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
        finally:
            print("STATUS: Crisis handled, security maintained\n")

    if (crisis_type == "routine_access"):
        try:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            with open(file_name, "r") as f:
                text = f.read()
            print(f"SUCCESS: Archive recovered - ``{text}''")
        except (FileNotFoundError, PermissionError):
            print("Error found.")
        finally:
            print("STATUS: Normal operations resumed\n")


def crisis_response():
    """send inputs to handle_crisis()"""

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    handle_crisis("lost_archive.txt", "archive_not_found")
    handle_crisis("classified_vault.txt", "denied_access")
    handle_crisis("standard_archive.txt", "routine_access")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == '__main__':
    crisis_response()
