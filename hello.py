def saluda(quien):
    """Corrige el resultado para que la función regrese un saludo de la forma:
    ¡Hola <quien>!
    """
    return "¡Hola!"


# Ignora por ahora esto, es sólo para que pruebes tu función.
if __name__ == "__main__":
    nombre = input("Nombre:")
    print(saluda(nombre))
