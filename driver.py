import os
import sys
from Utils.createpacketinfo import createpacketinfo
from Utils.printinfo import printallpacketinfo, printflaginfo

data = createpacketinfo()

while(1):
    print('1 - View information of all packets')
    print('2 - View packets with a particular TCP flag')
    print('c - Clear the screen')
    print('x - Exit')
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        print()
        printallpacketinfo(data)
    elif choice == '2':
        flag = input("Enter the TCP flag to display ('FIN', 'SYN', 'RST', 'PSH', 'ACK', 'URG'): ").upper()
        if flag not in ['FIN', 'SYN', 'RST', 'PSH', 'ACK', 'URG']:
            print('Please enter a valid flag!\n')
            continue
        printflaginfo(data, flag)
    elif choice == 'c':
        if os.name == 'nt':
            # Windows
            os.system('cls')
        else:
            # Linux or Mac
            os.system('clear')
    elif choice == 'x':
        print('Exiting program...')
        sys.exit()
    else:
        print('Please enter a valid option!\n')
