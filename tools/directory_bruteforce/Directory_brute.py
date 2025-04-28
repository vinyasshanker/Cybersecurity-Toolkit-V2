import subprocess
import os
import shlex
from urllib.parse import urlparse

class FUFF:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def validate_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    def ffuf(self, host):
        if not self.validate_url(host):
            print("[❌] Invalid URL. Please provide a valid URL (e.g., http://example.com)")
            return

        check = ["which", "ffuf"]
        check_res = subprocess.run(check, capture_output=True, text=True)

        if check_res.returncode != 0:
            print("[❌] FFUF is not installed on your system.")
            install_permission = input("Do you want to install it? (Y/N): ")

            if install_permission.lower() == 'y':
                subprocess.run(["sudo", "apt", "install", "ffuf"], check=True)
            else:
                print("Skipping installation.")
                return
        else:
            print("[✅] FFUF is already installed.")

        default_wordlist = os.path.join(self.base_dir, "/usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt")
        print("\nDefault wordlist:")
        print(f"-> {default_wordlist}")
        wordlist = input("Enter custom wordlist path or press Enter to use default: ").strip()

        if wordlist == "":
            wordlist = default_wordlist
        elif not os.path.isfile(wordlist):
            print("[❌] Wordlist file not found")
            return

        print("\n[Optional] Add any custom ffuf flags you want.")
        print("For example: -mc 200, -t 50, -fs 4242, -recursion\n")
        custom_flags = input("Enter custom flags or press Enter to skip: ").strip()

        cmd = ["ffuf", "-u", f"{host}/FUZZ", "-w", wordlist, "-c"]
        if custom_flags:
            cmd.extend(shlex.split(custom_flags))

        print("\n[👍] Final command to be executed:")
        print(" ".join(cmd))

        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output.strip())

            rc = process.poll()
            return rc
        except subprocess.CalledProcessError as e:
            print(f"[❌] Error running ffuf: {e}")
            return 1

class Feroxbuster:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def validate_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    def feroxbuster(self, host):
        if not self.validate_url(host):
            print("[❌] Invalid URL. Please provide a valid URL (e.g., http://example.com)")
            return

        check = ['which', 'feroxbuster']
        check_res = subprocess.run(check, capture_output=True, text=True)

        if check_res.returncode != 0:
            print("[❌] FEROXBUSTER is not installed. Do you want to install it?")
            install_permission = input("Y/N: ")

            if install_permission.lower() == 'y':
                subprocess.run(["sudo", "apt", "install", "feroxbuster"], check=True)
            else:
                print('[+] Skipping the installation')
                return
        else:
            print('[✅] Feroxbuster is installed')

        default_wordlist = os.path.join(self.base_dir, "/usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt")
        print("\nDefault wordlist:")
        print(f"-> {default_wordlist}")
        wordlist = input("Enter custom wordlist path or press Enter to use default: ").strip()

        if wordlist == "":
            wordlist = default_wordlist
        elif not os.path.isfile(wordlist):
            print("[❌] Wordlist file not found")
            return

        print("\n[Optional] Add any custom feroxbuster flags you want.")
        man = '''
            Response filters:
          -S, --filter-size <SIZE>...                 Filter out messages of a particular size
          -X, --filter-regex <REGEX>...               Filter out messages via regular expression matching
          -W, --filter-words <WORDS>...               Filter out messages of a particular word count
          -N, --filter-lines <LINES>...               Filter out messages of a particular line count
          -C, --filter-status <STATUS_CODE>...        Filter out status codes (deny list)
              --filter-similar-to <UNWANTED_PAGE>...  Filter out similar pages
          -s, --status-codes <STATUS_CODE>...         Status Codes to include (allow list)
        '''
        print(f"{man}")
        custom_flags = input("Enter custom flags or press Enter to skip: ").strip()

        cmd = ["feroxbuster", "-u", host, "-w", wordlist]
        if custom_flags:
            cmd.extend(shlex.split(custom_flags))

        print("\n[👍] Final command to be executed:")
        print(" ".join(cmd))

        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )

            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output.strip())

            rc = process.poll()
            return rc
        except subprocess.CalledProcessError as e:
            print(f"[❌] Error running feroxbuster: {e}")
            return 1