#En este archivo vamos a ver algo sobre condicionales
#Por ejemplo el tipico if
start=5
usuario="maria"
password="admin"
user=input("ingresa tu usuario \n")
passw=input("ingresa tu contraseña \n")

##esta es una tipica condicion if
#donde usas dos variables definida y la comparas con los ingresados por el usuario
# recuerde investigar los prefijos and or equal y otros prefijos de comparacion  que alla
#asi como las partes del esquema iff
if user==usuario and passw==password:
    state="Ha entrado a su dashboard"
else:
    state="Intente nuevamente"
print(state)
