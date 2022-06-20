import socket
import select
from thread import *
import sys
import time
import random
import threading
from timer import Timer

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IPaddress = str(sys.argv[1]) # first argument of the string as the IP Address

Port = int(sys.argv[2]) # second argument as the port number

server.bind((IPaddress, Port))

server.listen(100)

Q = [" What is the product of 2 and 3 ? \n a.1 b.5 c.3 d.6",
     " What is the sum of 20 and 39 ? \n a.69 b.59 c.19 d.-19",
     " What is the difference of 45 and 21 ? \n a.24 b.-24 c.66 d.-66",
     " What is the answer when 35 is divided by 5 ? \n a.5 b.7 c.175 d.35",
     " How many senses does a Human have ? \n a.3 b.4 c.5 d.6",
     " How many wonders are there in the world? \n a.7 b.8 c.10 d.4",
     " What is the first element of periodic table? \n a.H b.He c.Li d.Be",
     " How many states are there in India? \n a.24 b.29 c.30 d.31",
     " Who invented the telephone? \n a.A.G Bell b.John Wick c.Thomas Edison d.G Marconi",
     " What is the current influencing virus named? \n a.Corona b.COVID-19 c.HIV d.Flu",
     " Who is the present prime minister of India ? \n a.Manmohansingh b.Narendra modi c.Ramnadh Covind d.Rahul gandhi ",
     " What is the value of sin^2 a + cos^2 a? \n a.2 b.1 c.0 d.tan^2 a",
     " Where is TajMahal located ? \n a.Mumbai b.Agra c.Banglore d.USA",
     " How many players are there in a Cricket team ? \n a.6 b.12 c.9 d.11",
     " What is the captial of China ? \n a.Wuhan b.Bejing c.Hongkong d.NewDelhi",]

A = [ 'd', 'b', 'a', 'b', 'c', 'a', 'a', 'b', 'a', 'b', 'b', 'b', 'b', 'd', 'b' ]

Clients = []

Score=[]

client = ["CLIENT", 0]

buzzor = [0] 

Question = [0]

Won = [0]

Care = [0]

def Send(message):

    for clients in Clients:
        try:
            clients.send(message)
        except:
            clients.close()
            remove(clients)


def Buzzor(i) :
		
	Send("             TIME IS OVER !!  \n")
	Score[i] -= 0.5
	Send("             NO ANSWER  PLAYER " + str(i+1) + "  -0.5" + "\n"  )
	Send("             NEXT QUESTION WILL BE DISPLAYED IN FEW SECONDS   \n  ")
	time.sleep(2)
	buzzor[0] = 0
	Care[0] = 1


			
def Startquiz():

    if len(Q) != 0:
        Question[0] = random.randint(0,1000)%len(Q)
	Send(" \n     YOU HAVE ONLY  10 SECONDS TO PRESS THE BUZZOR \n ")
	print A[Question[0]][0]	

        for connection in Clients:
            connection.send(Q[Question[0]])
	
	while True :
	    time.sleep(10)
	    if buzzor[0] == 0 :
		if len(Q) != 0:
                       Q.pop(Question[0])
                       A.pop(Question[0])
                if len(Q)==0 or Won[0] == 1 :
                       Finishquiz()
                Care[0] = 0
                Startquiz()
	        break

 
def Finishquiz():

        Send("\n"+"                  GAME OVER \n ")
        
        for k in range(len(Clients)):
            Clients[k].send("               YOU SCORED  " + str(Score[k]) + " POINTS." +"\n")
	
	time.sleep(2)

        Send("BYE!!")
	print("\nExiting in Few seconds \n ")
	time.sleep(4)
	server.close()
        sys.exit()

        	
def remove(connection):

    	if connection in Clients:
        	Clients.remove(connection)



def clientthread(conn, addr):

    conn.send("    WELCOME TO THIS GAME SHOW !!\n")
    conn.send("    INSTRUCTIONS\n" )
    conn.send("    YOU WILL HAVE 10 SECONDS TO PRESS THE BUZZOR\n" )
    conn.send("    PRESS ANY KEY AND PRESS ENTER OR JUST PRESS ENTER FOR THE BUZZOR\n" )
    conn.send("    YOU WILL HAVE 10 SECONDS TO ANSWER AFTER PRESSING THE BUZZOR\n" )
    conn.send("    +1 FOR RIGHT ANSWER AND -0.5 FOR WRONG AND NO ANSWER\n" )
    conn.send("    TYPE THE OPTION  AND PRESS ENTER TO ANSWER\n")

    while True:

            message = conn.recv(2048)

            if message:
		
                if buzzor[0] == 0 and Care[0] == 0 and Care2[0] == 1 :
		    
                    client[0] = conn
                    buzzor[0]  = 1
                    i = 0

                    while i < len(Clients):
                            if Clients[i] == client[0]:
                                break
                            i +=1
                    client[1] = i

		    print("PLAYER  "+str(i+1)+"  PRESSED BUZZOR FIRST   ")
		    Send("          PLAYER  "+str(i+1)+"   PRESSED BUZZOR FIRST \n   ")
		    Clients[i].send("       YOU HAVE ONLY TEN SECONDS TO ANSWER  \n  ")
		    s = threading.Timer(10.0, Buzzor,[i]) # Timer after pressing the buzzor.
                    s.start()
		    
		    

                elif buzzor[0] == 1 and conn == client[0]:

                        s.cancel()

                        if message[0] == A[Question[0]][0] :

                            Send( "           RIGHT ANSWER   " + " PLAYER " + str(client[1]+1) + " +1" + "\n\n" )
                            Score[i] += 1
			    

                            if Score[i]>=5:

				Clients[i].send(     "          CONGRATULATIONS !!! YOU WON   \n \n  "                    )
                                Send(     "       PLAYER " + str(client[1]+1) + " WON THE GAME SHOW " + "\n"+"\n"  )
				Send(     "       WAIT FOR FEW SECONDS FOR  YOUR SCORE TO DISPLAY ")

                                Won[0] = 1
                             
			    else :
		
			        Send("           NEXT QUESTION WILL BE DISPLAYED IN FEW SECONDS  \n ")   

                        else:

                            Send("           WRONG ANSWER   " + "  PLAYER   " + str(client[1]+1) + "-0.5" + "\n\n")
                            Score[i] -= 0.5

			    Send("           NEXT QUESTION WILL BE DISPLAYED IN FEW SECONDS  \n ")

			time.sleep(2)
			buzzor[0]=0
			Care[0] = 1

Care2 = [0]

while True:

    conn, addr = server.accept()
    Clients.append(conn)
    Score.append(0)
    print  "Connected To " + " Player " + str(len(Clients)) 
    start_new_thread(clientthread,(conn,addr))

    if(len(Clients)==3):
	time.sleep(1)
	for k in range(len(Clients)):
            Clients[k].send(   "        YOU ARE PLAYER " + str(k+1)  )

	time.sleep(4)

	Send(" QUIZ IS ABOUT TO START IN 10 SECONDS ALL THE BEST !!! \n\n ")
	
	time.sleep(10)
	Care2[0] = 1
	Startquiz()

conn.close()
server.close()
