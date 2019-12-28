import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    nome = raw_input("Qual seu nome de usuario?\n")
    conectando_ip = raw_input("A que IPv4 voce deseja se conectar?\n")
    conectando_porta = int(raw_input("E a que porta deseja se conectar no ip: " + conectando_ip + "\n"))
    print "Aguardando resposta do ip: " + conectando_ip
    client.sendto("Voce deseja se conectar com: " + nome + "?(y/n)" + "\n", (conectando_ip, conectando_porta))
    msg, friend = client.recvfrom(1024)
    if msg == "y\n":
        print "Coneccao estabelecida."
        client.sendto("Conceccao estabelecida com: " + nome + ".\n", (conectando_ip, conectando_porta))
    else:
        client.sendto("Voce recusou esta coneccao.\nPrecione enter", (conectando_ip, conectando_porta))
        print "Coneccao recusada."
        client.shutdown(socket.SHUT_RDWR)
        client.close()

    while True:
        sua_msg = raw_input("Voce: ")
        if sua_msg == "sair":
            client.sendto("Conceccao finalizada.\nPrecione enter", (conectando_ip, conectando_porta))
            client.shutdown(socket.SHUT_RDWR)
            client.close()
        else:
            client.sendto(nome + ": " + sua_msg + "\n" + "Voce: ", (conectando_ip, conectando_porta))
            msg2, friend = client.recvfrom(1024)
            if msg2 == "sair\n":
                client.sendto("Voce saiu do chat com " + nome + ".\nPrecione enter", (conectando_ip, conectando_porta))
                client.shutdown(socket.SHUT_RDWR)
                client.close()
                print friend + " saiu do chat\nPrecione enter."
            else:
                print conectando_ip + ": " + msg2

except Exception as erro:
    client.shutdown(socket.SHUT_RDWR)
    client.close()
    print erro

