from passlib.context import CryptContext

contexto = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pdkdf2_sha256__default_rounds=20000,
)

texto = "gfhsjsskirinksks"
encriptado = contexto.hash(texto)
print(encriptado)
print(contexto.verify(texto, encriptado))