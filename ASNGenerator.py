##  ASN Generator
##  Generates 25 ASNs
##  Made By Abacus
import random
from random import randint
import time
import os
import sys
import colorama
from colorama import init
from colorama import Fore
from colorama import Fore, Back, Style
init()

banner = f'''
 █████╗ ███████╗███╗   ██╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔════╝████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████║███████╗██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔══██║╚════██║██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║  ██║███████║██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                              {Fore.RESET}┌─────────────────────────────────────┐
                              {Fore.RESET}│{Fore.BLUE}[{Fore.RESET}*{Fore.BLUE}] NOTE: NOT ALL ASNS WILL WORK! [{Fore.RESET}*{Fore.BLUE}]{Fore.RESET}│ 
                              {Fore.RESET}└─────────────────────────────────────┘{Fore.RESET}                                       
'''.replace('█', f'{Style.DIM}{Fore.BLUE}█{Fore.RESET}').replace('╗', f'{Fore.RESET}╗{Fore.RESET}').replace('║', f'{Fore.RESET}║{Fore.RESET}').replace('╚', f'{Fore.RESET}╚{Fore.RESET}').replace('═', f'{Fore.RESET}═{Fore.RESET}')

def asn(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
print(banner)
sys.stdout = open("ASNs.txt", "w")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
print(f"AS{asn(5)}")
sys.stdout.close()
os.system(f"echo {Fore.BLUE}Your ASNs Have Been Save Into ASNs{Fore.RESET}.{Fore.BLUE}txt!")