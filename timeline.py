import subprocess

def access_registry_editor():
    subprocess.run(["start", "regedit"], shell=True)

def navigate_to_hives():
    print("Please navigate to the following paths in the Registry Editor:")
    print("1. HKEY_LOCAL_MACHINE > SYSTEM > CurrentControlSet > Control > HiveList")
    print("2. HKEY_LOCAL_MACHINE > SOFTWARE")

def export_hive(key_path, hive_name):
    print(f"Exporting {hive_name} hive...")
    subprocess.run(["reg", "export", key_path, f"{hive_name}.reg"])

if __name__ == "__main__":
    access_registry_editor()
    navigate_to_hives()

    # Export System Hive
    system_key_path = "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\HiveList"
    export_hive(system_key_path, "System")

    # Export Software Hive
    software_key_path = "HKEY_LOCAL_MACHINE\\SOFTWARE"
    export_hive(software_key_path, "Software")

    print("Hive export completed.")
