class decoder():
     
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    def __init__(self,file_to_decode,key):
        self.file_to_decode = file_to_decode
        self.key = key
    
    def decode(self):
        file_to_decode = open(self.file_to_decode,"r")
        text_to_decode = file_to_decode.read()
        text_to_decode = text_to_decode.lower()
        decoded_text = ""
        for x in range(len(text_to_decode)):
            if(ord(text_to_decode[x]) == 32 or (ord(text_to_decode[x]) == 44) or (ord(text_to_decode[x]) == 46)):
                decoded_text += " "
            else:
                decoded_text += self.alphabet[(ord(text_to_decode[x])-97)-(ord(self.key)-97)]
        return decoded_text

    def saveToFile(decoded_text):
        saveFile = open("decodedFile.txt","w")
        saveFile.write(decoded_text)
        saveFile.close()