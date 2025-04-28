import subprocess

class Nmap:
    def __init__(self):
        pass

    def nmap(self, host):
        check = ['which', 'nmap']
        check_res = subprocess.run(check, capture_output=True, text=True)
        if check_res.returncode !=0:
            print("[❌] NMAP is not installed. Do you want to install it?")
            install_permission = input("Y/N: ")
            if install_permission.lower() == 'y':
                subprocess.run(["sudo", "apt", "install", "nmap"], check=True)
            else:
                print('[+] Skipping the installation')
                return
        else:
            print('[✅] Nmap is installed ')
        
        custom_flag = input("Enter custom flags for Nmap (or press Enter to skip): ")

        cmd = f"nmap {custom_flag} {host}"
        print(f"\n[👍] Final command to be executed: {cmd}")
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())

        rc = process.poll()
        return rc


class WhatWeb:
    def __init__(self):
        pass

    def whatweb(self, host):
        check = ['which', 'whatweb']
        check_res = subprocess.run(check, capture_output=True, text=True)
        if check_res.returncode !=0:
            print("[❌] WHATWEB is not installed. Do you want to install it?")
            install_permission = input("Y/N: ")
            if install_permission.lower() == 'y':
                subprocess.run(["sudo", "apt", "install", "whatweb"], check=True)
            else:
                print('[+] Skipping the installation')
                return
        else:
            print('[✅] WhatWeb is installed ')
        
        custom_flag = input("Enter custom flags for WhatWeb (or press Enter to skip): ")

        cmd = f"whatweb {custom_flag} {host}"
        print(f"\n[👍] Final command to be executed: {cmd}")
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())

        rc = process.poll()
        return rc
    
class Sublist3r:
    def __init__(self):
        pass

    def sublist3r(self, host):
        check = ['which', 'sublist3r']
        check_res = subprocess.run(check, capture_output=True, text=True)
        if check_res.returncode !=0:
            print("[❌] SUBLIST3R is not installed. Do you want to install it?")
            install_permission = input("Y/N: ")
            if install_permission.lower() == 'y':
                subprocess.run(["sudo", "apt", "install", "sublist3r"], check=True)
            else:
                print('[+] Skipping the installation')
                return
        else:
            print('[✅] Sublist3r is installed ')
        
        custom_flag = input("Enter custom flags for Sublist3r (or press Enter to skip): ")

        cmd = f"sublist3r -d {host} {custom_flag}"
        print(f"\n[👍] Final command to be executed: {cmd}")
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())

        rc = process.poll()
        return rc
    
class amassh:
    def __init__(self):
        pass

    def amassh(self, host):
        check = ['which', 'amass']
        check_res = subprocess.run(check, capture_output=True, text=True)
        if check_res.returncode !=0:
            print("[❌] AMASS is not installed. Do you want to install it?")
            install_permission = input("Y/N: ")
            if install_permission.lower() == 'y':
                subprocess.run(["sudo", "apt", "install", "amass"], check=True)
            else:
                print('[+] Skipping the installation')
                return
        else:
            print('[✅] Amass is installed ')
        
        custom_flag = input("Enter custom flags for Amass (or press Enter to skip): ")

        cmd = f"amass enum -d {host} {custom_flag}"
        print(f"\n[👍] Final command to be executed: {cmd}")
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())

        rc = process.poll()
        return rc

class EyeWitness:
    def __init__(self):
        pass

    def eyewitness(self, host):
        check = ['which', 'eyewitness']
        check_res = subprocess.run(check, capture_output=True, text=True)
        if check_res.returncode !=0:
            print("[❌] EYEWITNESS is not installed. Do you want to install it?")
            install_permission = input("Y/N: ")
            if install_permission.lower() == 'y':
                subprocess.run(["sudo", "apt", "install", "eyewitness"], check=True)
            else:
                print('[+] Skipping the installation')
                return
        else:
            print('[✅] EyeWitness is installed ')
        
        custom_flag = input("Enter custom flags for EyeWitness (or press Enter to skip): ")

        cmd = f"eyewitness {custom_flag} {host}"
        print(f"\n[👍] Final command to be executed: {cmd}")
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())

        rc = process.poll()
        return rc