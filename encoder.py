

class encoder():

    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    def __init__(self,file_to_encode,key):
        self.file_to_encode = file_to_encode
        self.key = key
    
    def encode(self):
        file_to_encode = open(self.file_to_encode,"r")
        text_to_encode = file_to_encode.read()
        text_to_encode = text_to_encode.lower()
        encoded_text = ""
        for x in range(len(text_to_encode)):
            if(ord(text_to_encode[x]) == 32 or (ord(text_to_encode[x]) == 44) or (ord(text_to_encode[x]) == 46)):
                encoded_text += " "
            else:
                encoded_text += self.alphabet[(ord(text_to_encode[x]) + ord(self.key) - (194) )% 26]
        return encoded_text
        
    def saveToFile(self,encoded_text):
        saveFile = open("encodedFile.txt","w")
        saveFile.write(encoded_text)
        saveFile.close()




