  
#!/use/bin/python3
import nmap
scanner=nmap -port scanner
print("welcome to venomsploit all in one tool")
print("<................................>")
 
ip_addr = input("enter the IP you want to scan:")
print("The IP address you enter is:",IP_addr)
type(ip_addr)

resp = input("""/n enter the type of scan you want to do
01)synack scan
02)UDP scan /n""")

if resp == '01':
print ("nmap version:",resp)
scanner.scan(ip_addr,'1-1024','-V -sS')
print(scanner.scaninfo())

