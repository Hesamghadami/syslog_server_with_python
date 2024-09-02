import socket
import logging 

logging.basicConfig(
    filename='sys.log',
    filemode='a',
                    )

logger = logging.getLogger()



port = 514
host = '192.168.10.2'

s = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)

s.bind((host,port))

while True:
    log, add = s.recvfrom(1024)
    logger.warning(f"{log.decode()} {add[0]}:{add[1]}")
