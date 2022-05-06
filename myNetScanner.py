import scapy.all as scapy
import subprocess
import optparse

def get_user_ip():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ip",dest="ipAddress",help="target ip adress")

    (user_input,arguments) = parse_object.parse_args()

    if not user_input.ipAddress:
        print("Enter Ip Address")

    return user_input

def netScanner(user_ip):

    arp_request_packet = scapy.ARP(pdst=user_ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()

def get_mac_address(ip):

    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1)[0]
    print(answered_list[0][1].hwsrc)

user_ip_address = get_user_ip()
netScanner(user_ip_address.ipAddress)




