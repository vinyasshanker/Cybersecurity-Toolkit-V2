import subprocess
import tempfile
import os

class JohnTheRipper:
    def __init__(self):
        pass

    def crack(self):
        """
        Uses John the Ripper to crack a single hash using a wordlist.
        """
        
        if subprocess.run(['which', 'john'], capture_output=True).returncode != 0:
            print("[❌] John the Ripper is not installed.")
            install = input("Do you want to install it? [Y/N]: ").strip().lower()
            if install == 'y':
                subprocess.run(['sudo', 'apt', 'install', 'john', '-y'], check=True)
            else:
                print("Skipping John installation.")
                return

        
        target_hash = input("Enter the hash to crack: ").strip()
        if not target_hash:
            print("No hash provided. Aborting.")
            return

        tmp_path = None
        try:
           
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
                tmp_file.write(target_hash)
                tmp_path = tmp_file.name

            
            formats = {1: 'raw-md5', 2: 'raw-sha1', 3: 'nt', 4: 'crypt', 5: 'sha256crypt'}
            print("Available hash formats:")
            for num, fmt in formats.items():
                print(f"[{num}] {fmt}")
            while True:
                try:
                    choice = int(input("Select format number: "))
                    selected_format = formats[choice]
                    break
                except (ValueError, KeyError):
                    print("Invalid choice, please try again.")

            
            default_wl = '/usr/share/wordlists/rockyou.txt'
            wordlist = input(f"Enter wordlist path (default: {default_wl}): ").strip() or default_wl
            if not os.path.isfile(wordlist):
                print(f"Wordlist {wordlist} does not exist. Aborting.")
                return

            
            custom_flags = input("Enter any additional flags (e.g., --rules), or leave blank: ").strip().split()

            
            cmd = ['john', f'--format={selected_format}', f'--wordlist={wordlist}', *custom_flags, tmp_path]
            print(f"[+] Executing: {' '.join(cmd)}")
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                print(line.strip())
            process.wait()

        finally:
            # Clean up temp file
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)


class Hashcat:
    def __init__(self):
        pass

    def crack(self):
        """
        Uses Hashcat to crack a single hash using a wordlist.
        """
       
        if subprocess.run(['which', 'hashcat'], capture_output=True).returncode != 0:
            print("[❌] Hashcat is not installed.")
            install = input("Do you want to install it? [Y/N]: ").strip().lower()
            if install == 'y':
                subprocess.run(['sudo', 'apt', 'install', 'hashcat', '-y'], check=True)
            else:
                print("Skipping Hashcat installation.")
                return

        
        target_hash = input("Enter the hash to crack: ").strip()
        if not target_hash:
            print("No hash provided. Aborting.")
            return

        tmp_path = None
        try:
            
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
                tmp_file.write(target_hash)
                tmp_path = tmp_file.name

            
            modes = {1: 0, 2: 1000, 3: 1800, 4: 1400}
            print("Available hash modes:")
            for num, mode in modes.items():
                print(f"[{num}] Mode {mode}")
            while True:
                try:
                    choice = int(input("Select mode number: "))
                    selected_mode = modes[choice]
                    break
                except (ValueError, KeyError):
                    print("Invalid choice, please try again.")

            
            default_wl = '/usr/share/seclists/Passwords/Leaked-Databases/rockyou-75.txt'
            wordlist = input(f"Enter wordlist path (default: {default_wl}): ").strip() or default_wl
            if not os.path.isfile(wordlist):
                print(f"Wordlist {wordlist} does not exist. Aborting.")
                return

           
            custom_flags = input("Enter any additional flags (e.g., -O), or leave blank: ").strip().split()

            
            cmd = ['hashcat', '-m', str(selected_mode), '-a', '0', *custom_flags, tmp_path, wordlist]
            print(f"[+] Executing: {' '.join(cmd)}")
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                print(line.strip())
            process.wait()

        finally:
            
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)
