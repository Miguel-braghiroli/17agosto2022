import hashlib
from hmac import digest

class Hash:
    def generateHash(h):
        digest = h.hexdigest()
        return digest

x = 0

while x < 1:
    print("Elija el algoritmo de hash a utilizar:")
    print("\n1. SHA256")
    print("2. SHA512")
    opcion = int(input("\nIngrese una opcion: "))
    algorythm = ""
    if opcion != 3:
        if opcion == 1:
            datos = input("\nIngrese los datos a hashear: ")
            algorythm = "SHA256"
        if opcion == 2:
            datos = input("\nIngrese los datos a hashear: ")
            algorythm = "SHA512"
        texto = bytes(datos, "utf-8")
        h = hashlib.new(algorythm, texto)
        hash1 = Hash.generateHash(h)
        print("\nEl hash es: " + hash1)
        x = 0
    else:
        x = 1
        

        
    
