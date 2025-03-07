from hello import saluda


def test_saludo():
    """Pruebas de saludo"""
    assert saluda("Yama") == "¡Hola Yama!"
    assert saluda("") == "¡Hola !"
