# Server-Client-Gameshow

GAME SHOW

DESCRIPTION OF THE GAME SHOW :

There is a host who conducts the show and three participants/players who provide answers. The host has a long list of questions and correct answers
with him. He randomly chooses one of the questions and sends to all three players. The players receive the question, think about the answer for a
while and press the buzzer. There is a timer for 10 seconds for buzzer to be presssed. Otherwise, the host moves on to the next question. The first one
to press the buzzer is given a chance to provide the answer within 10 seconds. If the answer is correct, he is given 1 point, otherwise -0.5.Nobody gets chance to answer this question again. The host then proceeds with the next question. The game stops when any player gets 5 points and that player is declared the winner.

INSTRUCTIONS TO RUN :

1. Download the files server.py and client.py in your system download the files in three other users also in if you are using three users ( participants ) other than this.

2. Run the command "python server.py < IP Address> <Any Port number>" on your terminal ( host ) after going into the respective directory in which the files are downloaded.

3. You can obtain the IP adress by using the command hostname -I in the terminal.

4. Open three more users or three more terminals ( participants )on your desktop and type python client.py < IP address> <Server's port number>
in each of them and proceed.

5. Then the game gets started and you can start answering the questions.

6. Press any button and press enter or just press enter for the buzzor.

7. Multiple choice questions will be present and you have to type the option and press enter for answering furthur instructions will be found
there and description of the game is given below.
  
DESCRIPTION OF THE CODE :

I have wrote two files server.py(for the host) , client.py(for the three participants) . First , When we run the command server.py it acts as host
and awaits for the clients(participants) to get connected . The paticipants will be alloted the names Player1,Player2,Player3 as per their respective
timeof paticipation . When the server gets connected a thread will be created by start_new_thread commandand similarly when other two get connected  and threads are created a client thread ( ) will be formed of three to send or recieve messages and run the game show . As soon as 3
clients are connected instructions will be displayed and quiz will be started by calling Startquiz() function .

A list of clients Clients[ ] will be maintained for furthur use . Score[ ] list will used to keep track of their scores . Question[ ] wil keep track of
question number and Buzzor [ ] for buzzor . Q[ ] contains a list of 15 questions and A[ ] has thier answers.Questions and answers are popped from  the list simultaneously whether it is answered or not answered . After the question is displayed it awaits for 10 sec for anyone to press the buzzor orelse it will go for next question . If anyone presses the buzzor then Buzzor value goes to 1 . An infinite while loop is used in te Start quiz function which will keep track of buzzor if the buzzor goes to zero then it will go for next question within few seconds . Answer for the displayed question will be displayed for the host .

After the buzzor is pressed a message is received in the thread the buzzor goes to one and the player number will be identified fron Clients [ ] and
his identity is stored in client [ ] a timer will start ( threading.Timer( ) taken from thrading module ) and if he gives answer timer will get cancelled then the answer will be checked with the option and increments the ( Score [ 1 , 2 , 3 ] ) if right and decrements if wrong and the buzzor goes to zero . If the paticipant does not answer after pressing the buzzor buzzor ( ) function will be called which decrements the players score for not answering and makes the buzzor [ ] to zero .If len(Q[ ]) goes to zero then the game will stop or if anyone gets 5 the participant wins and scores and the game will be ended by calling Finish quiz ( ) . Finish quiz ( ) willdisplay their respective scores , clients will also get exited and the server will also get closed and exited .
