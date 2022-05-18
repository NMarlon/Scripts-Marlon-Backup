#v0.0.1


import PIL
import pyautogui






myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'./data/megaInfo/testes/screenshot_test.png')


class bot:
      
    def printSys(what):
        print("system_body_bot: "+what)

        
    def perception(what):#External/Fisical ///## UPDATING Constant...
        if(what=="all"):
            bot.printSys("trying do perception all...")
        elif (what=="something new"):
            bot.printSys("trying to find something new...")


    def mental(self):#Know/internal/Spiritual/mental/imagination
        bot.printSys("thinking...")


    def myfunc(self):
        bot.printSys("Hello my whatISee is " + whatISee)

    def atuar(self, whatICanDo):#Power/Action/faith/believe/to doing
        bot.printSys("try to action")
                

        pyautogui.moveTo(-100, 100, duration = 0.5)

    def IDoSomething(self,what):
    	vaiFazerAlgo=False
    	perception(what)

    	if(not vaiFazerAlgo):
    		printSys("Desculpe, o bot não entendeu a solicitação")
    	
    def emotion():
    	printSys('Emotion... ')
    	#Felicidade, alegria :D :)
    	#Raiva >:(
    	#tristeza ;(
    	#medo <:8
    	#desprezo :/
    	#nojo >:P
    	#surpresa :o
    	

    	#Emotions
			#Felicidade: Atrai


    def __init__(self, whatISee, whatICanDo, name):
        self.whatISee = whatISee
        self.whatICanDo = whatICanDo
        print("system_body: thinking...")

        

        #IDLE:
            #Checar se está tudo OK!
        bot.see("all")
        return

    def awake(self):
    	printSys("Acordando bot "+self.name)


def printRoot(what):
    print("[SYS_root]: "+what)


megaMan = bot("","","megaMan")


def actionSys(what):
	if(what=="1"):
		megaMan.awake()


	elif(what=="2"):
	elif(what=="3"):
	elif(what=="4"):
	elif(what=="5"):
	elif(what=="6"):
	elif(what=="7"):
	elif(what=="8"):
	elif(what=="9"):
	elif(what=="10"):
	else:
		if(megaMan.IDoSomething(what)):
			printRoot("O bot não entendeu DIGITE UM VALOR VÁLIDO!")

while(True):
	printRoot("O que você deseja fazer?")
	printRoot("1 - acordar bot")
	printRoot("2 - falar com bot")
	printRoot("3 - ensinar o bot")
	printRoot("4 - treinar o bot")
	printRoot("5 - punir o bot")
	printRoot("")
	printRoot("")
	printRoot("")
	printRoot("")
	printRoot("")
	printRoot("")
	printRoot("9 - resetar bot")
	printRoot("")
	actionSys(input("Digite: "))