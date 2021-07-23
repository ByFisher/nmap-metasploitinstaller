import os
import from
banner=(""" cff00ccff
	dMMMMb  dMP dMP dMMMMMP dMP .dMMMb  dMP dMP dMMMMMP dMMMMb 
   dMP"dMP dMP.dMP dMP     amr dMP" VP dMP dMP dMP     dMP.dMP 
  dMMMMK"  VMMMMP dMMMP   dMP  VMMMb  dMMMMMP dMMMP   dMMMMK"  
 dMP.aMF dA .dMP dMP     dMP dP .dMP dMP dMP dMP     dMP"AMF   
dMMMMP"  VMMMP" dMP     dMP  VMMMP" dMP dMP dMMMMMP dMP dMP """)
print(banner)
print("""
	1-metasploiti indir
	2-nmapi kur""")
if == (1):
	os.system("clear")
	os.system("apt upgrade")
	os.system("apt update")
  os.system("pkg upgrade")
	os.system("pkg update")
	os.system("apt install curl")
	os.system("apt install wget")
	os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall")
if == (2):
	os.system("clear")
	os.system("apt upgrade")
	os.system("apt update")
  os.system("pkg upgrade")
	os.system("pkg update")
	os.system("pkg install nmap")
