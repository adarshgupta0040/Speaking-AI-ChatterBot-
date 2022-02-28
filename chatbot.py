from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp

engine=pp.init()
voice=engine.getProperty("voices")
print(voice)

engine.setProperty('voice', voice[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()


bot = ChatBot("My Bot")
convo = [
    'hey',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Adarsh',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in Kanpur',
    'In which language you talk?',
    ' I mostly talk in english',
    
    'Enter your full name',
    "Please wait",
    "i have a complain",
    "please ellabote",
    "i cannot login exam portal",
    "Kindly contact at this number 10001000 thank you"

]
trainer = ListTrainer(bot)
#now training the bot with help of trainer
trainer.train(convo)
#answer = bot.get_response("hi")
#print(answer)

#print("Talk to bot ")
#while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main=Tk()
main.geometry("500x600")
main.title("My ChatMate")
img = PhotoImage(file=r"E:\project\bot2.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msg.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msg.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msg.yview(END)

frame=Frame(main)
sc=Scrollbar(frame)
msg=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
#yscrollcommand=sc.set scrollbar get active after all messg start exceeding
sc.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()

#creating Function for enter button to send messgage
def enter_function(event):
    btn.invoke()

#going to bind main window with enter key
main.bind('<Return>', enter_function)


main.mainloop()


