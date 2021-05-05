print("""
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗████████╗██╗ ██████╗ ██████╗
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██║██╔════╝██╔═══██╗
██████╔╝███████║██║   ██║██╔██╗ ██║█████╗     ██║   ██║██║     ██║   ██║
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝     ██║   ██║██║     ██║   ██║
██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗   ██║   ██║╚██████╗╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═════╝
The phonetic alphabet, but easier.
Enter a word/phrase to begin""")
#Phonetic (nato) alphabet below:
phoneticalphabet = {'a':'Alpha', 'b':'Bravo','c':'Charlie', 'd':'Delta', 'e':'Echo', 'f':'Foxtrot', 'g':'Golf', 'h':'hotel', 'i':'India', 'j':'Juliet', 'k':'Kilo', 'l':'Lima', 'm':'Mike', 'n':'November', 'o':'Oscar', 'p':'Papa', 'q':'Quebec', 'r':'Romeo', 's':'Sierra', 't':'Tango', 'u':'Uniform', 'v':'Victor', 'w':'Whiskey', 'x':'X-ray', 'y':'Yankee', 'z':'Zulu'}

userinput = input(": ")
for letter in userinput:
   print(phoneticalphabet.get(letter.lower()), end=' ')
