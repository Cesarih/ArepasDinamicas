# Bienvenida al usuario
print("¡Hola! Bienvenido al programa para calcular la cantidad de masa para arepas.")

# Solicitar al usuario la cantidad de harina en gramos
harina = input("¿Cuántos gramos de harina usará?: ")
# Convertir la entrada del usuario a un número entero
harina = int(harina)

# Solicitar al usuario la cantidad de agua en mililitros
agua = input("¿Cuántos mililitros de agua usará?: ")
# Convertir la entrada del usuario a un número entero
agua = int(agua)

# Solicitar al usuario la cantidad de sal en gramos
sal = input("¿Cuántos gramos de sal usará?: ")
# Convertir la entrada del usuario a un número entero
sal = int(sal)

# Calcular la cantidad total de masa
masa_total = harina + agua + sal

# Mostrar la cantidad total de masa al usuario
print("La cantidad total de masa para sus arepas es:", masa_total, "gramos")

# Despedida al usuario
print("¡Disfrute sus arepas!")