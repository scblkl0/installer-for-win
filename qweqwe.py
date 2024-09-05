import os
import sys
import msvcrt
import subprocess
import urllib.request


def install_winget():
    print("Checking for winget...")
    try:
        subprocess.run(["where", "winget"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("winget is already installed.")
    except subprocess.CalledProcessError:
        print("winget not found. Installing winget...")
        winget_installer_url = "https://aka.ms/getwinget"
        temp_installer_path = os.path.join(os.getenv('TEMP'), "wingetInstaller.exe")
        print("Downloading winget installer...")
        urllib.request.urlretrieve(winget_installer_url, temp_installer_path)
        print("Installing winget...")
        subprocess.run(["powershell", "-Command",
                        f"Start-Process -FilePath {temp_installer_path} -ArgumentList '/silent', '/norestart'"
                        f" -NoNewWindow -Wait"],
                       check=True)
        try:
            subprocess.run(["where", "winget"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("winget installed successfully.")
        except subprocess.CalledProcessError:
            print("winget installation failed. Please install it manually.")
            sys.exit(1)


def wait_for_key_press():
    print("\nPress any key to return to the menu...", end='', flush=True)
    msvcrt.getch()
    os.system('cls')


def main_menu():
    os.system('cls')
    print(
        "MAIN MENU                                                                                    for vyga by vyga")
    print("\nChoose: 1 - Browsers, 2 - Soft, 3 - Install/Uninstall all, Escape - Exit")


def browser_menu():
    while True:
        os.system('cls')
        print("Choose the browser:")
        print("1 - Mozilla Firefox")
        print("2 - Google Chrome")
        print("3 - OperaGX")
        print("4 - Opera")
        print("\nEscape - Return to Main Menu")
        print(
            "------------------------------------------------------------------------------------------------------")

        choice = msvcrt.getch()
        if choice == b'1':
            install_or_uninstall("Mozilla Firefox", "Mozilla.Firefox")

        elif choice == b'2':
            install_or_uninstall("Google Chrome", "Google.Chrome")

        elif choice == b'3':
            install_or_uninstall("OperaGX", "XPDBZ4MPRKNN30")

        elif choice == b'4':
            install_or_uninstall("Opera", "Opera.Opera")

        elif choice == b'\x1b':
            return


def soft_menu():
    while True:
        os.system('cls')
        print("1 - Telegram")
        print("2 - Discord")
        print("3 - Steam")
        print("4 - OBS")
        print("5 - Notepad++")
        print("6 - GIMP")
        print("7 - ShareX")
        print("\nEscape - Return to Main Menu")
        print(
            "-----------------------------------------------------------------------------------------------------")

        choice = msvcrt.getch()
        if choice == b'1':
            install_or_uninstall("Telegram", "Telegram.TelegramDesktop")
            
        elif choice == b'2':
            install_or_uninstall("Discord", "Discord.Discord")

        elif choice == b'3':
            install_or_uninstall("Steam", "Valve.Steam")
            
        elif choice == b'4':
            install_or_uninstall("OBS", "OBSProject.OBSStudio")

        elif choice == b'5':
            install_or_uninstall("Notepad++", "Notepad++.Notepad++")

        elif choice == b'6':
            install_or_uninstall("GIMP", "GIMP.GIMP")

        elif choice == b'7':
            install_or_uninstall("ShareX", "ShareX.ShareX")

        elif choice == b'\x1b':
            return


def install_or_uninstall(program_name, winget_id):
    os.system('cls')
    print(f"1 - Install {program_name}")
    print(f"2 - Uninstall {program_name}")
    print("\nEscape - Return to Previous Menu")
    print(
        "-----------------------------------------------------------------------------------------------------")

    choice = msvcrt.getch()
    if choice == b'1':
        print(f"\nYou will install {program_name}")
        print("\nEnter - continue, esc - abort")
        confirmation = msvcrt.getch()
        if confirmation == b'\r':
            os.system(f"winget install {winget_id}")
            wait_for_key_press()

    elif choice == b'2':
        print(f"\nYou will uninstall {program_name}")
        print("\nEnter - continue, esc - abort")
        confirmation = msvcrt.getch()
        if confirmation == b'\r':
            os.system(f"winget uninstall {winget_id}")
            wait_for_key_press()

    elif choice == b'\x1b':
        return


def install_uninstall_all():
    os.system('cls')
    print("1 - Install all programs")
    print("2 - Uninstall all programs")
    print("\nEscape - Return to Main Menu")
    print(
        "-----------------------------------------------------------------------------------------------------")

    choice = msvcrt.getch()
    if choice == b'1':
        install_all()
    elif choice == b'2':
        uninstall_all()
    elif choice == b'\x1b':
        return


def install_all():
    os.system('cls')
    print("Installing all programs:")
    os.system("winget install Mozilla.Firefox")
    os.system("winget install Google.Chrome")
    os.system("winget install XPDBZ4MPRKNN30")
    os.system("winget install Opera.Opera")
    os.system("winget install Telegram.TelegramDesktop")
    os.system("winget install Discord.Discord")
    os.system("winget install Valve.Steam")
    os.system("winget install OBSProject.OBSStudio")
    os.system("winget install Notepad++.Notepad++")
    os.system("winget install GIMP.GIMP")
    os.system("winget install ShareX.ShareX")
    print("All programs installed.\nPress any key to return to the main menu...", end='', flush=True)
    msvcrt.getch()


def uninstall_all():
    os.system('cls')
    print("Uninstalling all programs:")
    os.system("winget uninstall Mozilla.Firefox")
    os.system("winget uninstall Google.Chrome")
    os.system("winget uninstall XPDBZ4MPRKNN30")
    os.system("winget uninstall Opera.Opera")
    os.system("winget uninstall Telegram.TelegramDesktop")
    os.system("winget uninstall Discord.Discord")
    os.system("winget uninstall Valve.Steam")
    os.system("winget uninstall OBSProject.OBSStudio")
    os.system("winget uninstall Notepad++.Notepad++")
    os.system("winget uninstall GIMP.GIMP")
    os.system("winget uninstall ShareX.ShareX")
    print("All programs uninstalled.\nPress any key to return to the main menu...", end='', flush=True)
    msvcrt.getch()


def main():
    while True:
        main_menu()
        main_menu_choice = msvcrt.getch()
        if main_menu_choice == b'1':
            browser_menu()
        elif main_menu_choice == b'2':
            soft_menu()
        elif main_menu_choice == b'3':
            install_uninstall_all()
        elif main_menu_choice == b'\x1b':
            return
        else:
            continue


if __name__ == "__main__":
    install_winget()
    main()
