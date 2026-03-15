import win32com.client 
import os 

def say(text):
    os.system(f"say {text}")
    
if __name__ == '__main__':
    print("Starting the program...")
    say("Hello, how are you?")