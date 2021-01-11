#!/usr/bin/env python3

import dns.resolver
from colorama import Fore, Style
import argparse


bold = '\033[1m'
green = bold + Fore.GREEN
red = bold + Fore.RED
reset = Style.RESET_ALL

def check_record(domain, record):
    try:
        record = dns.resolver.query(domain.strip(),record)
        if record:
            return True
        
    except dns.exception.DNSException:
        return False

parser = argparse.ArgumentParser(description="Usage: python3 lookup.py -f domains.file")
parser.add_argument('-f','--file',dest="domains",help="File with domains to check")
parsed = parser.parse_args()

domains = open(parsed.domains,'r').read().splitlines()

with open('active.txt','w') as active, open('dormant.txt','w') as dormant:
    for domain in domains:
        if not check_record(domain,'A') and not check_record(domain,'CNAME') and not check_record(domain,'MX'):
            print(red + 'DORMANT ' + reset + domain)
            dormant.write(domain + '\n')
        else:
            print(green + 'ACTIVE ' + reset + domain)
            active.write(domain + '\n')
