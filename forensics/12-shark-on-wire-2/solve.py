from scapy.all import rdpcap

cap = rdpcap("./interesting.pcap")
flag = ""
for i in cap:
    flag += chr(i.sport - 5000)

print(flag)
