import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC address')
    parser.add_option('-m', '--mac', dest='x', help='New MAC address')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] Please write down interface. --help, -h for more info')
    elif not options.x:
        parser.error('[-] Please write down MAC address. --help, -h for more info')
    return options


def change_mac(interface, x):
    print('[+] Changing MAC address for', interface, 'to', x)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', x])
    subprocess.call(['ifconfig', interface, 'up'])


def check_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', options.interface])
    ifconfig_result = ifconfig_result.decode('utf - 8')
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('[-] Could not read MAC address.')


options = get_arguments()

current_mac = check_mac(options.interface)
print(f'Current MAC: {current_mac}')
change_mac(options.interface, options.x)

current_mac = check_mac(options.interface)
if current_mac == options.x:
    print(f'[+] MAC address successfully changed to {current_mac}.')
else:
    print(f'[-] MAC address did not get changed.')


def write_file(filepath):
    with open(filepath, 'w') as file:
        x = file.write(f'MAC: {options.x}\n')
    file.close()


def read_file(filepath):
    with open(filepath, 'r') as f_o:
        return f_o.readlines()