import json
import ipaddress

deviceJSON = '{"Version": "15.6", "locationN": "500 Northridge", "role": "Access", "upTime": "12:10:53.49", "hostname": "ATL-3650-1", "macAddress": "39:58:1f:9e:38:c1", "series": "Cisco Catalyst 3650 Series Switches", "lastUpdated": "2017-09-21 13:12:46", "bootDateTime": "2016-10-27 05:24:53", "interfaceCount": "24", "lineCardCount": "1", "managementIpAddress": "192.168.10.10", "interfaces": {"interface": [{"GigabitEthernet0": {"ipv4": "100.100.100.1"}}, {"GigabitEthernet1": {"ipv4": "10.10.10.2"}}]}}'

device = json.loads(deviceJSON)

for interface in device['interfaces']['interface']:
    for name, ip in interface.items():
        int_ip = ip['ipv4']
        if ipaddress.ip_address(int_ip).is_private:
            print(f'{name} has an ip address of {int_ip} is a Private Address.')
        else:
            print(f'{name} has an ip address of {int_ip} is not a Private Address.')