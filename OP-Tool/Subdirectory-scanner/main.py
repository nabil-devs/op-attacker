import requests


def domain_scanner(domain, direc):
    print('URLS FOUND:')
    
    for directory in direc:
        url = f"https://{domain}/{directory}"
        
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                print(f'[+] {url}')
            
        except requests.ConnectionError:
            pass
 

print("MADE BY UNKNOWN")

print("Please only enter domain")
domain = input("Enter the Domain Name: ")

with open('list.txt','r') as file:
        name = file.read()

         
        directory = name.splitlines()