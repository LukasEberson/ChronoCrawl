import os
import sys
import time
import pandas as pd
from url_checker import check_urls
from input_parser import load_urls_from_file
from exporter import export_results

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear()
    print(r"""
_________ .__                               _________                      .__   
\_   ___ \|  |_________  ____   ____   ____ \_   ___ \____________ __  _  _|  |  
/    \  \/|  |  \_  __ \/  _ \ /    \ /  _ \/    \  \/\_  __ \__  \\ \/ \/ /  |  
\     \___|   Y  \  | \(  <_> )   |  (  <_> )     \____|  | \// __ \\     /|  |__
 \______  /___|  /__|   \____/|___|  /\____/ \______  /|__|  (____  /\/\_/ |____/
        \/     \/                  \/               \/            \/             

        Made with <3 by Lukas Eberson and ChatGPT
    """)
    print("==== ChronoCrawl MENU ====")
    print("1. Load URLs from file")
    print("2. Start URL check")
    print("3. Export results")
    print("4. Exit")

def choose_file():
    path = input("Enter path to your file (.txt/.csv/.xlsx): ").strip()
    if not os.path.exists(path):
        print("File not found.")
        return None
    try:
        urls = load_urls_from_file(path)
        if urls:
            print(f"Loaded {len(urls)} URLs.")
            return urls
    except Exception as e:
        print("Error loading file:", e)
    return None

def choose_export(results):
    if not results:
        print("No results to export.")
        return
    print("Choose export format:")
    print("1. CSV")
    print("2. Excel")
    choice = input("Your choice: ").strip()
    if choice == "1":
        export_results(results, 'csv')
    elif choice == "2":
        export_results(results, 'xlsx')
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    url_list = []
    results = []

    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            url_list = choose_file()
            input("Press Enter to continue...")
        elif choice == "2":
            if not url_list:
                print("You need to load URLs first.")
            else:
                print("Checking URLs... (this may take some time)")
                print("⚠️  Don't close this terminal while the scan is running...")
                results = check_urls(url_list)
                print("Check completed.")
            input("Press Enter to continue...")
        elif choice == "3":
            choose_export(results)
            input("Press Enter to continue...")
        elif choice == "4":
            print("Exiting ChronoCrawl. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")
