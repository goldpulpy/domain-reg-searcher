from app import DomainSearcher
from texts import Info_block, Menu, EnterForContinue, GenerateBlock, Logo
from colorama import Fore, Style
from threading import Thread
import os




app = DomainSearcher()

def CheckDomain(domain,tld):
    if app.CheckDomain(domain, tld):
        print(f"{domain}.{tld} {Fore.GREEN}is available{Style.RESET_ALL}")
        with open("domains.txt", "a") as output_file:
            output_file.write(f"{domain}.{tld}\n")





def main():
    while True:
        os.system('cls')



        Logo()
        Info_block(app.GetWordList(),app.GetDomainList(), app.GetTLDList())
        Menu()
        try:
            choice = int(input("Enter your choice: "))


            if choice == 1:
                word_list = []
                while True:
                    os.system('cls')
                    print(f"{Fore.BLUE}Words added: {Style.RESET_ALL}"+ ", ".join(word_list))
                    print(f'{Fore.YELLOW}Type {Fore.GREEN}/back {Fore.YELLOW}to back or {Fore.GREEN}/file {Fore.YELLOW}for load words from file{Style.RESET_ALL}')
                    word_for_add = input(f'Enter word: ')
                    word_for_add = word_for_add.lower()
                    if word_for_add != "/back" and word_for_add != "/file":
                        word = app.AddWord(word_for_add)
                        word_list.append(word)

                    elif word_for_add == "/file":
                        word_file_path = input("Enter file path: ")
                        try:
                            counts = app.AddWordFile(word_file_path)
                            print(f"{counts} {Fore.GREEN}words added successfully{Style.RESET_ALL}")
                            EnterForContinue()
                            break
                        except FileNotFoundError:
                            print(f"{Fore.RED}File {Style.RESET_ALL}{word_file_path}{Fore.RED} not found{Style.RESET_ALL}")
                            EnterForContinue()
                        except PermissionError:
                            print(f"{Fore.RED}File {Style.RESET_ALL}{word_file_path}{Fore.RED} has no permission{Style.RESET_ALL}")
                            EnterForContinue()
                    
                    elif word_for_add == "/back":
                        EnterForContinue()
                        break
            elif choice == 2:
                tld_list = []
                while True:
                    os.system('cls')
                    print(f"{Fore.BLUE}TLDs added: {Style.RESET_ALL}"+ ", ".join(tld_list))
                    print(f'{Fore.YELLOW}Type {Fore.GREEN}/back {Fore.YELLOW}to back or {Fore.GREEN}/file {Fore.YELLOW}for load TLDs from file{Style.RESET_ALL}')
                    tld_for_add = input(f'Enter TLD: ')
                    tld_for_add = tld_for_add.lower()
            
                    if tld_for_add != "/back" and tld_for_add != "/file":
                        tld = app.AddTLD(tld_for_add)
                        tld_list.append(tld)

                    elif tld_for_add == "/file":
                        tld_file_path = input("Enter file path: ")
                        try:
                            counts = app.AddTLDFile(tld_file_path)
                            print(f"{counts} {Fore.GREEN}TLDs added successfully{Style.RESET_ALL}")
                            EnterForContinue()
                            break
                        except FileNotFoundError:
                            print(f"{Fore.RED}File {Style.RESET_ALL}{tld_file_path}{Fore.RED} not found{Style.RESET_ALL}")
                            EnterForContinue()
                        except PermissionError:
                            print(f"{Fore.RED}File {Style.RESET_ALL}{tld_file_path}{Fore.RED} has no permission{Style.RESET_ALL}")
                            EnterForContinue()
                    
                    elif tld_for_add == "/back":
                        EnterForContinue()
                        break
            elif choice == 3:
                domain_list = []
                while True:
                    os.system('cls')
                    print(f"{Fore.BLUE}Domains added: {Style.RESET_ALL}"+ ", ".join(domain_list))
                    print(f'{Fore.YELLOW}Type {Fore.GREEN}/back {Fore.YELLOW}to back or {Fore.GREEN}/file {Fore.YELLOW}for load domains from file{Style.RESET_ALL}')
                    domain_for_add = input(f'Enter domain: ')
                    domain_for_add = domain_for_add.lower()
                    if domain_for_add != "/back" and domain_for_add != "/file":
                        domain = app.AddDomain(domain_for_add)
                        domain_list.append(domain)

                    elif domain_for_add == "/file":
                        domain_file_path = input("Enter file path: ")
                        try:
                            counts = app.AddDomainFile(domain_file_path)
                            print(f"{counts} {Fore.GREEN}words added successfully{Style.RESET_ALL}")
                            EnterForContinue()
                            break
                        except FileNotFoundError:
                            print(f"{Fore.RED}File {Style.RESET_ALL}{domain_file_path}{Fore.RED} not found{Style.RESET_ALL}")
                            EnterForContinue()
                        except PermissionError:
                            print(f"{Fore.RED}File {Style.RESET_ALL}{domain_file_path}{Fore.RED} has no permission{Style.RESET_ALL}")
                            EnterForContinue()
                    
                    elif domain_for_add == "/back":
                        EnterForContinue()
                        break



            elif choice == 4:
                os.system('cls')

                while True:
                    os.system('cls')
                    GenerateBlock()
                    choice = int(input("Enter your choice: "))
                    if choice < 5:
                        counts = app.Generate(choice)
                        print(f"{counts} {Fore.GREEN}domain names added{Style.RESET_ALL}")
                        EnterForContinue()
                    else:
                        print(f"{Fore.YELLOW}Back to Menu{Style.RESET_ALL}")
                        EnterForContinue()
                        break

            elif choice == 5:
                os.system('cls')
                threads = int(input("Enter number of threads: "))
                print(f"{Fore.YELLOW}Start searching domain for register...{Style.RESET_ALL}")
                print(Fore.MAGENTA+"================================"+Style.RESET_ALL)
                domain_list = app.GetDomainList()
                tld_list = app.GetTLDList()



                output_file = open("domains.txt", "w"); output_file.close()
                
                if threads > len(domain_list): threads = len(domain_list)

                th_list = []
                for domain in range(len(domain_list)):
                    for tld in range(len(tld_list)):
                        th = Thread(target=CheckDomain, args=(domain_list[domain],tld_list[tld]))
                        th_list.append(th)
                        if len(th_list) == threads:
                            for th in th_list:
                                th.start()
                            for th in th_list:
                                th.join()
                            th_list = []
                for th in th_list:
                    th.start()
                for th in th_list:
                    th.join()
                print(Fore.MAGENTA+"================================"+Style.RESET_ALL)
                print(f"{Fore.YELLOW}Domain search completed{Style.RESET_ALL}")



                EnterForContinue()



        except ValueError:
            print(f"{Fore.RED}Please enter a number{Style.RESET_ALL}")
            EnterForContinue()
        

    


try:
    main()
except KeyboardInterrupt:
    print(f"{Fore.RED}Program terminated{Style.RESET_ALL}")
except Exception as e:
    print(f"{Fore.RED}Unknown error: {e}{Style.RESET_ALL}")