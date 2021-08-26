import socket

from select import select
from random import randint
from loguru import logger

logger.remove()
logger.add("info.log", format="{time} {level} {message}", level="INFO")

servers = [] 

for port in range(8000,8002):
	ds = ("0.0.0.0", port)
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind(ds)
	server.listen()

	servers.append(server)

identifiers = {}
while True:
	readable, _, _ = select(servers, [], [])
	for s in readable:
		connection, addr = s.accept()
		if int(s.getsockname()[1]) == 8000: #если клиент стучится на 8000
			print("Got a connection from %s" % str(addr))
					
			msg = connection.recv(1024)
			msg = msg.decode('utf-8')
			uniq_code = str(randint(1, 100000))
			identifiers[msg]= uniq_code
			msg = ('\r\nВы присоединились к серверу \r\n'+\
					'Ваш идентификатор : {0} \r\n'+\
					'Ваш уникальный код: {1}').format(msg,uniq_code)

			connection.send(msg.encode('utf-8'))
			connection.close()

		if int(s.getsockname()[1]) == 8001: #если клиент стучится на 8001
			print("Got a connection from %s" % str(addr))
			
			msg = connection.recv(1024)
			msg = msg.decode('utf-8')
			msg = msg.split('/&$/')
			
			for key, value in identifiers.items():
				if key==msg[0] and value == msg[1]:
					logger.info('Сообщение: {}'.format(msg[2]))
					msg = "\r\nСообщение \"{}\" записано в лог".format(msg[2])
					connection.send(msg.encode('utf-8'))
				else:
					continue
			msg = ("\r\nВы ввели неправильный " + \
				"идентификатор или уникальный код")
			connection.send(msg.encode('utf-8'))
			connection.close()
