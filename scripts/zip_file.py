import subprocess
import os

def create_rar(file_to_archive, output_rar):
    rar_exe = r"C:\Program Files\WinRAR\WinRAR.exe"
    if not os.path.exists(rar_exe):
        print(f"WinRAR executable not found at {rar_exe}")
        return
    
    command = [rar_exe, "a", output_rar, file_to_archive]
    subprocess.run(command, check=True)


