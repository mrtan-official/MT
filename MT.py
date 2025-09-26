import os, platform, time, sys
print('\n\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Checking For Update...')
os.system('git pull')
print('\n\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m Follow My Github')
time.sleep(2)
os.system('xdg-open https://github.com/mrtan-official')
bit = platform.architecture()[0]
if bit == '64bit':
    print('\033[1;31m[\x1b[38;5;156m●\033[1;31m]\x1b[38;5;156m You are 64 Bit user')
    time.sleep(3)
    os.system("clear") 
    import wix
    #while True:
       # print('                          Tool is off')
else:
    print("32bit tool is not available now.\nPlease contact admin")
    os.system("xdg-open https://facebook.com/MrT4n.official")
