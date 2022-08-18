from werkzeug.security import generate_password_hash, check_password_hash

text = "fasdadfadsf3434fsd"

encriptado = generate_password_hash(text)
print("")
encriptado2 = generate_password_hash(text, "sha512")
print("")
encriptado3 = generate_password_hash(text, "pbkdf2:sha256:30", 30)
print(encriptado)
print(encriptado2)
print(encriptado3)

print(check_password_hash(encriptado, text))
print(check_password_hash(encriptado2, text))