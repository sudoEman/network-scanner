# ------------------------------------------
# NETWORK SCANNER
# ------------------------------------------


import socket
import sys

#------------------------------------------
# 1. INPUT SECTION:
# ------------------------------------------

tar = input("enter your targets ip")
start = int(input("enter you ports start range"))
end = int(input("enter your ports end range"))

#------------------------------------------
# 2.PORTS SERVICE NAMES:
#------------------------------------------

services = {
        21 : "Ftp",
        22 : "Ssh",
        23 : "Telnet",
        25 : "SMTP",
        42 : "WINS Replication",
        43 : "WHOIS",
        53 : "DNS",
        67 : "DHCP",
        68 : "DHCP",
        70 : "Gopher",
        80 : "HTTP",
        88 : "Kerberos",
        102 : "Microsoft Exchange ISO-TSAP",
        110 : "POP3",
        113 : "Ident",
        119 : "NNTP",
        123 : "NTP",
        137 : "NetBIOS-ns",
        138 : "NetBIOS-dgm",
        143 : "IMAP",
        161 : "SNMP-agents (unencrypted)",
        162 : "SNMP-trap (unencrypted)",
        179 : "BGP",
        194 :"IRC",
        201 : "ApplrTalk",
        264 : "BGMP",
        318 : "TSP",
        381 : "HP Openview",
        383 : "HP Openview-HP data alarm manager",
        411 : "(Multiple uses)",
        412 : "(Multiple uses)",
        427 : "SLP",
        443 : "HTTPS",
        445 : "Microsoft DS SMB",
        464 : "Kerberos",
        465 : "SMTP over TLS/SSL, SSM",
        497 : "Dantz Retrospect",
        500 : "IPSec / ISAKMP / IKE",
        512 : "rexec",
        513 : "rlogin",
        514 : "syslog",
        515 : "LPD/LPR",
        520 : "RIP",
        521 : "RIPng (IPv6)",
        540 : "UUCP",
        548 : "AFP",
        554 : "RTSP",
        546	: "DHCPv6",
        547 : "DHCPv6",
        560 : "rmonitor",
        563 : "NNTP over TLS/SSL",
        587 : "SMTP",
        591 : "File Maker",
        593 : "Microsoft DCOM",
        596 : "SMSD",
        631 : "IPP",
        636 : "LDAP over TLS/SSL",
        691 : "Microsoft Exchange",
        860 : "iSCSI",
        873 : "rsync",
        902 : "VMware Server",
        989 : "FTPS",
        990 : "FTPS",
        993 : "IMAP over SSL (IMAPS)",
        995 : "POP3 over SSL (POP3S)"
} 

for ports in range(start,end + 1):

   service = services.get(ports, "Unknown")

#------------------------------------------
# 3. PORTS CONNECTION CHECKING:
#------------------------------------------

   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   s.settimeout(5)
   result = s.connect_ex((tar,ports))
   if result == 0:
        print(f"{ports} : {service} -> open")
   else:
        print(f"{ports} : {service} -> close")

#-----------------------------------------
#4.CLOSING PORTS:
#----------------------------------------


   s.close()