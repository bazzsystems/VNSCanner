import subprocess
import platform
import os
import socket
import time
#import nmap 
#from nmap import PortScanner
#from nmap import *
#nm = PortScanner()
# Print welcome message
print("Welcome to VNSCanner, a tool to check for vulnerabilities in your system.")
print ("This tool is designed to run on Windows 10, And Requires Administrator Privileges.")
print("Press Enter to continue...")
input()
print("Script started at", time.strftime("%H:%M:%S", time.localtime()))
clear = lambda: os.system('cls')
time.sleep(1)
clear()
print("The script will check for updates, scan for viruses and malware, check for vulnerabilities, and print a report if any suspicious files or devices are found.")
time.sleep(1)
print("Starting scan...")
time.sleep(1)
clear()

# Check if system is up to date
print("Checking for updates...")
subprocess.run(["powershell.exe", "Get-WindowsUpdateLog"], shell=True)


input1 = input("Would you like to check for vulnerabilities it could take upto a 60 seconds? (y/n): ")
if input1 == "y":
    print("Checking for vulnerabilities...")
    subprocess.run(["sfc", "/scannow"], shell=True)
else:
    print("Skipping vulnerability check")

# Scan for viruses and malware
print("Scanning for viruses and malware...")
subprocess.run(["powershell.exe", "Get-MpThreatDetection"], shell=True)

# Print IP address of system
print("IP address:", socket.gethostbyname(socket.gethostname()))

# Print OS and system architecture
print("OS:", platform.system())
print("Architecture:", platform.machine())

# Print list of connected devices
print("Connected devices:")
output = subprocess.run(["arp", "-a"], stdout=subprocess.PIPE).stdout.decode()
print(output)

# Print list of running services
print("Running services:")
output = subprocess.run(["sc", "query"], stdout=subprocess.PIPE).stdout.decode()
print(output)

# Scan for open ports
#print("Scanning for open ports...")
#nm = nmap.PortScanner()
#scan_results = nm.scan(hosts='127.0.0.1', arguments='-sV')
#print("Open ports:")
#for host in scan_results['scan']:
#    for port in scan_results['scan'][host]['tcp']:
#        print(f"Port: {port}: Service: {scan_results['scan'][host]['tcp'][port]['name']}")

# Check for unauthorized users
print("Checking for unauthorized users...")
output = subprocess.run(["net", "user"], stdout=subprocess.PIPE).stdout.decode()
print(output)


input2 = input("Would you like to check for system logs it could take 1-5 minutes? (y/n): ")
if input2 == "y":
    print("Checking for system logs...")
    output = subprocess.run(["powershell.exe", "Get-EventLog -LogName System"], stdout=subprocess.PIPE).stdout.decode()
    print(output)
else:
    print("Skipping system log check")

# Check for running processes
print("Checking for running processes...")
output = subprocess.run(["tasklist"], stdout=subprocess.PIPE).stdout.decode()
print(output)

# Check for open ports
#print("Checking for open ports...")
#output = subprocess.run(["nmap", "-sT", socket.gethostbyname(socket.gethostname())], stdout=subprocess.PIPE).stdout.decode()
#print(output)

# Check for unauthorized users
print("Checking for unauthorized users...")
output = subprocess.run(["net", "user"], stdout=subprocess.PIPE).stdout.decode()
print(output)

# Check for system logs
print("Checking system logs for suspicious activity...")
output = subprocess.run(["powershell.exe", "Get-EventLog -LogName System -Newest 50"], stdout=subprocess.PIPE).stdout.decode()
print(output)

# Check for running processes
print("Checking for suspicious processes...")
output = subprocess.run(["tasklist"], stdout=subprocess.PIPE).stdout.decode()
print(output)

# Check for system configurations
print("Checking for misconfigurations in system settings...")
output = subprocess.run(["powershell.exe", "Get-ItemProperty HKLM:\Software\Policies\Microsoft\WindowsFirewall\DomainProfile"], stdout=subprocess.PIPE).stdout.decode()
print(output)

# Print report
print("Scan complete. See report below:")
print("Updates:")
print("Vulnerabilities:")
print("Viruses and malware:")
print("IP address:", socket.gethostbyname(socket.gethostname()))
print("OS:", platform.system())
print("Architecture:", platform.machine())
print("Connected devices:", output)
print("Running services:", output)
#print("Open ports:", output)
print("Unauthorized users:", output)
print("System logs:", output)
print("Running processes:", output)
print("Open ports:", output)
print("Unauthorized users:", output)
print("System logs:", output)
print("Suspicious processes:", output)
print("Misconfigurations in system settings:", output)

# Save report to text file
with open('report.txt', 'w') as f:
    f.write("Updates:")
    f.write("Vulnerabilities:")
    f.write("Viruses and malware:")
    f.write("IP address:" + socket.gethostbyname(socket.gethostname()))
    f.write("OS:" + platform.system())
    f.write("Architecture:" + platform.machine())
    f.write("Connected devices:" + output)
    f.write("Running services:" + output)
#    f.write("Open ports:" + output)
    f.write("Unauthorized users:" + output)
    f.write("System logs:" + output)
    f.write("Running processes:" + output)
    f.write("Open ports:" + output)
    f.write("Unauthorized users:" + output)
    f.write("System logs:" + output)
    f.write("Suspicious processes:" + output)
    f.write("Misconfigurations in system settings:" + output)


# save output to csv file
with open('report.csv', 'w') as f:
    f.write("Updates:")
    f.write("Vulnerabilities:")
    f.write("Viruses and malware:")
    f.write("IP address:" + socket.gethostbyname(socket.gethostname()))
    f.write("OS:" + platform.system())
    f.write("Architecture:" + platform.machine())
    f.write("Connected devices:" + output)
    f.write("Running services:" + output)
#    f.write("Open ports:" + output)
    f.write("Unauthorized users:" + output)
    f.write("System logs:" + output)
    f.write("Running processes:" + output)
    f.write("Open ports:" + output)
    f.write("Unauthorized users:" + output)
    f.write("System logs:" + output)
    f.write("Suspicious processes:" + output)
    f.write("Misconfigurations in system settings:" + output)

# Print end message
print("Script ended at", time.strftime("%H:%M:%S", time.localtime()))
print("Press Enter to exit...")
input()

#Orel Mizrahi Adani 03.01.2023
