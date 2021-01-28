import encoder 
import decoder

ec = encoder.encoder("test.txt","g")

print(ec.encode())
ec.saveToFile(ec.encode())

de = decoder.decoder("encodedFile.txt","g")
print(de.decode())
ec.saveToFile(de.decode())