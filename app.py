import pyautogui as pg
import time
import keyboard

greeter = """
 ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████                 
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒               
▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒               
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░               
 ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░               
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░                
  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░                
  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒                 
      ░  ░   ░                  ░ ░                 
                                                    
▄▄▄█████▓▓██   ██▓ ██▓███   ██▓ ███▄    █   ▄████   
▓  ██▒ ▓▒ ▒██  ██▒▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒  
▒ ▓██░ ▒░  ▒██ ██░▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░  
░ ▓██▓ ░   ░ ▐██▓░▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓  
  ▒██▒ ░   ░ ██▒▓░▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒  
  ▒ ░░      ██▒▒▒ ▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒   
    ░     ▓██ ░▒░ ░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░   
  ░       ▒ ▒ ░░  ░░        ▒ ░   ░   ░ ░ ░ ░   ░   
          ░ ░               ░           ░       ░   
          ░ ░                                       
 ▄▄▄▄ ▓██   ██▓    █     █░ ▒█████   ██▓      █████▒
▓█████▄▒██  ██▒   ▓█░ █ ░█░▒██▒  ██▒▓██▒    ▓██   ▒ 
▒██▒ ▄██▒██ ██░   ▒█░ █ ░█ ▒██░  ██▒▒██░    ▒████ ░ 
▒██░█▀  ░ ▐██▓░   ░█░ █ ░█ ▒██   ██░▒██░    ░▓█▒  ░ 
░▓█  ▀█▓░ ██▒▓░   ░░██▒██▓ ░ ████▓▒░░██████▒░▒█░    
░▒▓███▀▒ ██▒▒▒    ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒░▓  ░ ▒ ░    
▒░▒   ░▓██ ░▒░      ▒ ░ ░    ░ ▒ ▒░ ░ ░ ▒  ░ ░      
 ░    ░▒ ▒ ░░       ░   ░  ░ ░ ░ ▒    ░ ░    ░ ░    
 ░     ░ ░            ░        ░ ░      ░  ░        
      ░░ ░                                          
"""
print(greeter)

def check_user_input(input):
    try:
        # Convert it into integer
        return int(input)
    except ValueError:
        try:
            # Convert it into float
            return float(input)
        except ValueError:
            print("Input is not a number.\nSet for 5 as default.")
            return 5
def option_1(num, text, timeout):
    import time
    print('Starting after 5 seconds.\nHold (esc) to cancel!')
    if keyboard.is_pressed("esc"):
        i = num
        print("ended.")
    time.sleep(5)

    i = 0
    while i != num:
        if keyboard.is_pressed("esc"):
            i = num
            print("ended.")
            break
        i = i+1
        pg.press('Enter')
        pg.write(str(text))
        pg.press('Enter')
        time.sleep(timeout)
        print(str(i) + ' Done')
def option_2(timeout, texts):
    import time
    print('Starting after 5 seconds.\nHold (esc) to cancel!')
    time.sleep(5)

    for text in texts:
        if keyboard.is_pressed("esc"):
            i = num
            print("ended.")
            break
        pg.write(str(text))
        pg.press('Enter')
        time.sleep(timeout)
        print(str(i) + ' Done')

try:
    options = input("\nOptions:\n[1] Add one sentence that will be auto send\n[2] Add different sentence that will be auto send\nType the option number to start.\n")
except EOFError:
    option = 5
    print('Input is EOF exception, please enter something and run me again')
    exit()
except KeyboardInterrupt:
    option = 5
    print('You have pressed ctrl-c button.')
    exit()

options = check_user_input(options)

if options == 1:
    Num = input("How many times do you want to send the text?\n")
    Num = check_user_input(Num)
    text = input("Please type the text to send.\n")
    Timeout = input("Please type the time in seconds between every text. (0 for no timeout)\n")
    Timeout = check_user_input(Timeout)
    option_1(Num, text, Timeout)
elif options == 2:
    Num = input("How much texts do you want to send?\n")
    Num = check_user_input(Num)
    Timeout = input("Please type the time in seconds between every text. (0 for no timeout)\n")
    Timeout = check_user_input(Timeout)
    Texts = []
    i = 0
    while len(Texts) != Num:
        i = i+1
        text = input("Type text number ({i}):\n".format(i=i))
        Texts.append(text)
    option_2(Timeout, Texts)
else:
    print("Unknown input please try again later!")

pg.alert(text='The program ended', title='Done', button='Ok')