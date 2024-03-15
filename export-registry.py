import subprocess

# Define the path to the registry key you want to extract
registry_key = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion"

# Define the path where you want to save the exported registry file
export_path = "C:\\Temp\\exported_registry.reg"

# Run the reg save command to export the registry key
command = f'reg save "{registry_key}" "{export_path}"'
subprocess.run(command, shell=True)

print(f"Registry key '{registry_key}' exported and saved to '{export_path}'.")