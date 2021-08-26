import socket

def main():
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	host, port = socket.gethostname(), 8001                           

	connection.connect((host, port))                               

	msg1 = input('Введите свой идентификатор: ')
	msg2 = input('Введите свой уникальный код: ')
	msg3 = input('Введите текстовое сообщение: ')
	msg = msg1+ '/&$/' + msg2+ '/&$/' + msg3


	connection.send(msg.encode('utf-8'))
	
	msg = connection.recv(1024)   
	print(msg.decode('utf-8'))
	
	connection.close()

if __name__ == '__main__':
	main()