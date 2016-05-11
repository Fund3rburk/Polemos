import socket
import os
import sys
from datetime import datetime

# Clear
os.system('cls' if os.name == 'nt' else 'clear')

# Request host
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)


# start time for scanner
scanStart = datetime.now()

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)


try:
    for port in range(1, 300):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
scanStop = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
scanTime = scanStop - scanStart

# Printing the information to screen
print("Scanning Completed in: ", scanTime)
