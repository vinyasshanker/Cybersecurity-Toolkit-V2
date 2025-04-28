import os
import subprocess
import time
from tools.Secure_System.update_system import Update_System
from tools.Secure_System.update_system import Upgrade_System
from tools.directory_bruteforce.Directory_brute import FUFF
from tools.directory_bruteforce.Directory_brute import Feroxbuster
from tools.info_gathering.info_gather import Nmap
from tools.info_gathering.info_gather import WhatWeb
from tools.info_gathering.info_gather import Sublist3r
from tools.info_gathering.info_gather import amassh
from tools.info_gathering.info_gather import EyeWitness
from tools.password_crack.Password_Crack import JohnTheRipper
from tools.password_crack.Password_Crack import Hashcat
try:
    from colorama import init, Fore, Style
except ImportError:
    print("Colorama is not installed. Installing it now...")
    subprocess.run(["pip", "install", "colorama"], check=True)
    from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)

def clear_screen():
    os.system('clear')

# Hacker-themed ASCII banner with your name and GitHub
BANNER = f"""
{Fore.GREEN + Style.BRIGHT}╔════════════════════════════════════════════╗
{Fore.GREEN + Style.BRIGHT}║         Cybersecurity Toolkit v1.0         ║
{Fore.GREEN + Style.BRIGHT}╚════════════════════════════════════════════╝
{Fore.CYAN + Style.BRIGHT}  Created by: VINYAS 
{Fore.CYAN + Style.BRIGHT}  GitHub: https://github.com/vinyasshanker
{Fore.RED + Style.BRIGHT}  [+] Hack the Planet! [+]
{Fore.YELLOW}  Your ultimate tool for system security,
  information gathering, and more!
{Fore.GREEN + Style.BRIGHT}══════════════════════════════════════════════{Style.RESET_ALL}
"""

def display_hacker_animation(text):
    """Display text statically without typing animation."""
    clear_screen()
    print(text)  # Display the banner instantly
    time.sleep(0.5)  # Brief pause before menu

while True:
    display_hacker_animation(BANNER)
    print(f"{Fore.BLUE + Style.BRIGHT}Select option:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] Secure System{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[2] Information Gathering{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[3] Directory Bruteforce{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[4] Password Bruteforce{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[5] Burpsuite Pro{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[6] AI Chatbot{Style.RESET_ALL}")
    print(f"{Fore.RED}[99] Exit{Style.RESET_ALL}")

    try:
        i = int(input(f"{Fore.YELLOW + Style.BRIGHT}Please choose an option: {Style.RESET_ALL}"))

        match i:
            case 1:
                while True:
                    clear_screen()
                    print(BANNER)
                    print(f"{Fore.BLUE + Style.BRIGHT}Secure System Menu:{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}[1] Update System{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}[2] Upgrade System{Style.RESET_ALL}")
                    print(f"{Fore.RED}[99] Back to Main Menu{Style.RESET_ALL}")
                    i1 = int(input(f"{Fore.YELLOW + Style.BRIGHT}Enter choice: {Style.RESET_ALL}"))

                    match i1:
                        case 1:
                            print(f"{Fore.CYAN + Style.BRIGHT}You chose Update System{Style.RESET_ALL}")
                            updater = Update_System()
                            command = "sudo apt-get update".split()
                            print(updater.run_tool(command))
                            input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

                        case 2:
                            print(f"{Fore.CYAN + Style.BRIGHT}You chose Upgrade System{Style.RESET_ALL}")
                            upgrader = Upgrade_System()
                            command = "sudo apt-get full-upgrade".split()
                            print(upgrader.run_tool(command))
                            input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

                        case 99:
                            break

                        case _:
                            print(f"{Fore.RED + Style.BRIGHT}Invalid sub-option selected{Style.RESET_ALL}")
                            input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

            case 2:
                clear_screen()
                print(BANNER)
                print(f"{Fore.BLUE + Style.BRIGHT}Information Gathering Selected{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[1] Nmap{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[2] WhatWeb{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[3] Sublist3r{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[4] Amass{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[5] EyeWitness{Style.RESET_ALL}")
                print(f"{Fore.RED}[99] Back to Main Menu{Style.RESET_ALL}")
                try:
                    i3 = int(input(f"{Fore.YELLOW + Style.BRIGHT}Enter the option: {Style.RESET_ALL}"))
                    match i3:
                        case 1:
                            print(f"\n{Fore.CYAN + Style.BRIGHT}Nmap Scan{Style.RESET_ALL}")
                            print(f"{Fore.CYAN}---------{Style.RESET_ALL}")
                            host = input(f"{Fore.YELLOW + Style.BRIGHT}Please enter the target URL (e.g., http://example.com or 10.10.11.26): {Style.RESET_ALL}")
                            updater = Nmap()
                            result = updater.nmap(host)
                            if result is not None:
                                input(f"{Fore.YELLOW}\nScan complete. Press Enter to continue...{Style.RESET_ALL}")
                            
                        case 2:
                            print(f"\n{Fore.CYAN + Style.BRIGHT}WhatWeb Scan{Style.RESET_ALL}")
                            print(f"{Fore.CYAN}------------{Style.RESET_ALL}")
                            host = input(f"{Fore.YELLOW + Style.BRIGHT}Please enter the target URL (e.g., http://example.com): {Style.RESET_ALL}")
                            updater = WhatWeb()
                            result = updater.whatweb(host)
                            if result is not None:
                                input(f"{Fore.YELLOW}\nScan complete. Press Enter to continue...{Style.RESET_ALL}")
                            
                        case 3:
                            print(f"\n{Fore.CYAN + Style.BRIGHT}Sublist3r Scan{Style.RESET_ALL}")
                            print(f"{Fore.CYAN}---------------{Style.RESET_ALL}")
                            host = input(f"{Fore.YELLOW + Style.BRIGHT}Please enter the target URL (e.g., example.com): {Style.RESET_ALL}")
                            updater = Sublist3r()
                            result = updater.sublist3r(host)
                            if result is not None:
                                input(f"{Fore.YELLOW}\nScan complete. Press Enter to continue...{Style.RESET_ALL}")
                            
                        case 4:
                            print(f"\n{Fore.CYAN + Style.BRIGHT}Amass Scan{Style.RESET_ALL}")
                            print(f"{Fore.CYAN}-----------{Style.RESET_ALL}")
                            host = input(f"{Fore.YELLOW + Style.BRIGHT}Please enter the target URL (e.g., example.com): {Style.RESET_ALL}")
                            updater = amassh()
                            result = updater.amassh(host)
                            if result is not None:
                                input(f"{Fore.YELLOW}\nScan complete. Press Enter to continue...{Style.RESET_ALL}")
                            
                        case 5:
                            print(f"\n{Fore.CYAN + Style.BRIGHT}EyeWitness Scan{Style.RESET_ALL}")
                            print(f"{Fore.CYAN}----------------{Style.RESET_ALL}")
                            host = input(f"{Fore.YELLOW + Style.BRIGHT}Please enter the target URL (e.g., http://example.com): {Style.RESET_ALL}")
                            updater = EyeWitness()
                            result = updater.eyewitness(host)
                            if result is not None:
                                input(f"{Fore.YELLOW}\nScan complete. Press Enter to continue...{Style.RESET_ALL}")
                            
                        case 99:
                            break

                        case _:
                            print(f"{Fore.RED + Style.BRIGHT}Invalid sub-option selected{Style.RESET_ALL}")
                            input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED + Style.BRIGHT}Please enter a valid number{Style.RESET_ALL}")
                    input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
                except KeyboardInterrupt:
                    print(f"{Fore.RED + Style.BRIGHT}\nOperation cancelled by user{Style.RESET_ALL}")
                    input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED + Style.BRIGHT}\nAn error occurred: {str(e)}{Style.RESET_ALL}")
                    input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

            case 3:
                while True:
                    clear_screen()
                    print(BANNER)
                    print(f"{Fore.BLUE + Style.BRIGHT}Directory BruteForce Tool Menu:{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}[1] FFUF{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}[2] Feroxbuster{Style.RESET_ALL}")
                    print(f"{Fore.RED}[99] Back to Main Menu{Style.RESET_ALL}")
                    try:
                        i2 = int(input(f"{Fore.YELLOW + Style.BRIGHT}Enter the option: {Style.RESET_ALL}"))

                        match i2:
                            case 1:
                                print(f"\n{Fore.CYAN + Style.BRIGHT}FFUF Directory Bruteforce{Style.RESET_ALL}")
                                print(f"{Fore.CYAN}------------------------{Style.RESET_ALL}")
                                host1 = input(f"{Fore.YELLOW + Style.BRIGHT}Please enter the target URL (e.g., http://example.com): {Style.RESET_ALL}")
                                updater1 = FUFF()
                                result = updater1.ffuf(host1)
                                if result is not None:
                                    input(f"{Fore.YELLOW}\nScan complete. Press Enter to continue...{Style.RESET_ALL}")
                                
                            case 2:
                                print(f"\n{Fore.CYAN + Style.BRIGHT}Feroxbuster Directory Scan{Style.RESET_ALL}")
                                print(f"{Fore.CYAN}-------------------------{Style.RESET_ALL}")
                                host2 = input(f"{Fore.YELLOW + Style.BRIGHT}Enter the target URL (e.g., http://example.com): {Style.RESET_ALL}")
                                updater2 = Feroxbuster()
                                result = updater2.feroxbuster(host2)
                                if result is not None:
                                    input(f"{Fore.YELLOW}\nScan complete. Press Enter to continue...{Style.RESET_ALL}")
                                
                            case 99:
                                break
                            
                            case _:
                                print(f"{Fore.RED + Style.BRIGHT}Invalid sub-option selected{Style.RESET_ALL}")
                                input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

                    except ValueError:
                        print(f"{Fore.RED + Style.BRIGHT}Please enter a valid number{Style.RESET_ALL}")
                        input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
                    except KeyboardInterrupt:
                        print(f"{Fore.RED + Style.BRIGHT}\nOperation cancelled by user{Style.RESET_ALL}")
                        input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
                    except Exception as e:
                        print(f"{Fore.RED + Style.BRIGHT}\nAn error occurred: {str(e)}{Style.RESET_ALL}")
                        input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

            case 4:
                while True:
                    clear_screen()
                    print(BANNER)
                    print(f"{Fore.BLUE + Style.BRIGHT}Password Bruteforce Menu:{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}[1] John the Ripper{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}[2] Hashcat{Style.RESET_ALL}")
                    print(f"{Fore.RED}[99] Back to Main Menu{Style.RESET_ALL}")
                    try:
                        i4 = int(input(f"{Fore.YELLOW + Style.BRIGHT}Enter choice: {Style.RESET_ALL}"))
                        match i4:
                            case 1:
                                print(f"\n{Fore.CYAN + Style.BRIGHT}John the Ripper Selected{Style.RESET_ALL}")
                                tool = JohnTheRipper()
                                tool.crack()
                                input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
                            case 2:
                                print(f"\n{Fore.CYAN + Style.BRIGHT}Hashcat Selected{Style.RESET_ALL}")
                                tool = Hashcat()
                                tool.crack()
                                input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
                            case 99:
                                break
                            case _:
                                print(f"{Fore.RED + Style.BRIGHT}Invalid option{Style.RESET_ALL}")
                                input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
                    except ValueError:
                        print(f"{Fore.RED + Style.BRIGHT}Please enter a valid number{Style.RESET_ALL}")
                        input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
                    except KeyboardInterrupt:
                        print(f"{Fore.RED + Style.BRIGHT}\nOperation cancelled by user{Style.RESET_ALL}")
                        input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
                    except Exception as e:
                        print(f"{Fore.RED + Style.BRIGHT}\nAn error occurred: {str(e)}{Style.RESET_ALL}")
                        input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
            
            case 5:
                clear_screen()
                print(BANNER)
                print(f"{Fore.CYAN + Style.BRIGHT}Burpsuite Pro Selected{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Under Development{Style.RESET_ALL}")
                input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

            case 6:
                clear_screen()
                print(BANNER)
                print(f"{Fore.CYAN + Style.BRIGHT}AI Chatbot Selected{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Under Development{Style.RESET_ALL}")
                input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")

            case 99:
                print(f"{Fore.RED + Style.BRIGHT}Exiting program. Goodbye!{Style.RESET_ALL}")
                break

            case _:
                print(f"{Fore.RED + Style.BRIGHT}Invalid main option selected{Style.RESET_ALL}")
                input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED + Style.BRIGHT}Please enter a valid number{Style.RESET_ALL}")
        input(f"{Fore.YELLOW}\nPress Enter to continue...{Style.RESET_ALL}")