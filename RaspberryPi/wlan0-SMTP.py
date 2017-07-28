import socket
import smtplib
#import fcntl
import struct

#you connect the raspberry pi to internet using an ethernet cable of the wifi network directly
#/ or using your own personal router using ethernet cable

#issue is to find the ip address of the raspberry pi of the interface connected
#to internet via wifi

#raspberry pi connected to the ethernet cable of personal router and wlan0
#raspberry pi is also connected to the wireless network

#Method1:
#host name of the machine
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('www.google.com', 1))
print("ip address")
print(s.getsockname()[0])

#The above method is not fool proof and can give wrong results since we do not know which interface is WLAN0
#Use system calls to get this done
#http://code.activestate.com/recipes/439094-get-the-ip-address-associated-with-a-network-inter/

#Method 2:
#WLAN0 = 'wlan0'
#WLAN0 = WLAN0[:15]
#socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', WLAN0)))

#Method3: execute commands that are executed on the shell trhough code for the
#appropriate OS
#https://ubuntuforums.org/showthread.php?t=1215042
#http://elinux.org/RPi_Email_IP_On_Boot_Debian

#sending mail using SMTP
server = smtplib.SMTP('smtp.gmail.com',587)
#this SMTP server does not work
server = smtplib.SMTP('smtp.googlemail.com',465)

#secure connection and login
server.ehlo()
server.starttls()
server.login("gowri.r@gmail.com", "sahanakumar")

#print(socket.gethostbyname(socket.gethostname()))
msg = s.getsockname()[0] #socket.gethostbyname(socket.gethostname());

#send mail and quit
server.sendmail("gowr.i@gmail.com", "gowri.r@gmail.com", msg);
print("sent email")
server.quit();

#To allow less secure apps to access gmail
#https://myaccount.google.com/lesssecureapps?pli=1



