import socket

def main():
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	host, port = socket.gethostname(), 8000                           

	connection.connect((host, port))                               

	msg = input('Введите свой идентификатор: ')
	connection.send(msg.encode('utf-8'))
	
	msg = connection.recv(1024)   
	print(msg.decode('utf-8'))
	
	connection.close()

if __name__ == '__main__':
	main()