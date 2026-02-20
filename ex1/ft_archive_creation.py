def ft_archive_creation():
    """creates an .txt archive and writes inside"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name = "new_discovery.txt"
    try:
        print(f"🗃️  Initializing new storage unit: {file_name}")
        file = open(file_name, "x")
        print("Storage unit created successfully...✅\n")

        print("Inscribing preservation data...")
        entry1 = "{[}ENTRY 001{]} New quantum algorithm discovered"
        entry2 = "{[}ENTRY 002{]} Efficiency increased by 347%"
        entry3 = "{[}ENTRY 003{]} Archived by Data Archivist trainee"

        file.write(f"{entry1}\n")
        print(f"{entry1}")

        file.write(f"{entry2}\n")
        print(f"{entry2}")

        file.write(f"{entry3}")
        print(f"{entry3}\n")

        print("✅ Data inscription complete. Storage unit sealed.")
        print(f"Archive {file_name} ready for long-term preservation.")
    except FileExistsError:
        print("❌ Error: File already exists")


if __name__ == '__main__':
    ft_archive_creation()
