##  ASN Lookup
##  Looks up ASNs
##  Made By Abacus
import requests
import colorama
from colorama import init
from colorama import Fore
from colorama import Fore, Back, Style
init()

BANNER = f'''
 █████╗ ███████╗███╗   ██╗    ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██╔════╝████╗  ██║    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
███████║███████╗██╔██╗ ██║    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██╔══██║╚════██║██║╚██╗██║    ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
██║  ██║███████║██║ ╚████║    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                    {Fore.RESET}┌────────────────────────────┐
                    {Fore.RESET}│{Fore.BLUE}[{Fore.RESET}*{Fore.BLUE}] ASN LOOKUP BY ABACUS [{Fore.RESET}*{Fore.BLUE}]{Fore.RESET}│ 
                    {Fore.RESET}└────────────────────────────┘{Fore.RESET}                                       
'''.replace('█', f'{Style.DIM}{Fore.BLUE}█{Fore.RESET}').replace('╗', f'{Fore.RESET}╗{Fore.RESET}').replace('║', f'{Fore.RESET}║{Fore.RESET}').replace('╚', f'{Fore.RESET}╚{Fore.RESET}').replace('═', f'{Fore.RESET}═{Fore.RESET}')
def request_info(url):
	request = requests.get(url)
	response = request.text
	for line in response.splitlines():
            print(f'{line}')
print(BANNER)
asn = input("Enter ASN: ")
url = f"https://api.hackertarget.com/aslookup/?q={asn}"
response = requests.get(url)
if response.status_code == 200:
	request_info(url)
else:
	print("API Error!")