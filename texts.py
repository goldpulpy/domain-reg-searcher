from colorama import Fore, Style


def Logo():
        print(Fore.YELLOW+f"""
     (     (     
   ( )\ )  )\ )  
 ( )(()/( (()/(
 )((_)(_)) /(_))
((_)(_))_ (_))    
 | _ )   \| _ \ {Fore.CYAN}Domain REG Searcher{Style.RESET_ALL}{Fore.YELLOW} 
 | _ \ |) |  _/ {Fore.MAGENTA}Created by {Style.RESET_ALL}@goldpulpy{Fore.YELLOW}   
 |___/___/|_|   """+Style.RESET_ALL)


def Info_block(WordList, DomainList, TLDsList):
    print(Fore.MAGENTA+"================================"+Style.RESET_ALL)
    print("    Words for generation: " + Fore.GREEN + str(len(WordList)) + Style.RESET_ALL)
    print("            Domain names: " + Fore.GREEN + str(len(DomainList)) + Style.RESET_ALL)
    print("Top Level Domains (TLDs): " + Fore.GREEN + str(len(TLDsList)) + Style.RESET_ALL)
    print(Fore.MAGENTA+"================================"+Style.RESET_ALL)


def Menu():
    print(f"1. {Fore.YELLOW}Add words{Style.RESET_ALL}")
    print(f"2. {Fore.YELLOW}Add TLDs{Style.RESET_ALL} ({Fore.BLUE}Top Level Domain{Style.RESET_ALL})")
    print(f"3. {Fore.YELLOW}Add Domain names{Style.RESET_ALL}")
    print(f"4. {Fore.GREEN}Generate Domain names from words{Style.RESET_ALL}")
    print(f"5. {Fore.GREEN}Check Domain names{Style.RESET_ALL} [output to file]")
    print(Fore.MAGENTA+"================================"+Style.RESET_ALL)


def GenerateBlock():
    print(f"1. {Fore.YELLOW}Add one word{Style.RESET_ALL}")
    print(f"2. {Fore.YELLOW}Concatenate two words{Style.RESET_ALL}")
    print(f"3. {Fore.YELLOW}Concatenate three words{Style.RESET_ALL}")
    print(f"4. {Fore.YELLOW}Concatenate four words{Style.RESET_ALL}")
    print(f"5. {Fore.YELLOW}Back{Style.RESET_ALL}")

def EnterForContinue():
    print(f"\n{Fore.YELLOW}Press {Style.RESET_ALL}Enter {Fore.YELLOW}to continue...{Style.RESET_ALL}")
    input()

