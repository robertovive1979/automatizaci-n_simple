import re

def sanitizar(texto):
    """
    Limpia y normaliza el texto ingresado por el usuario para extraer
    el nombre de una empresa, ticker o entidad relevante.

    Ejemplos:
        "¿Cuál es el precio de una acción de Microsoft?" -> "microsoft"
        "Precio de Apple" -> "apple"
        "acción de Tesla" -> "tesla"
    """

    texto = texto.lower().strip()

    # Eliminar signos de puntuación comunes
    texto = re.sub(r"[¿?¡!,.;:]", "", texto)

    # Frases comunes que no forman parte del nombre de la empresa
    expresiones = [
        r"cu[aá]l es",
        r"cu[aá]nto cuesta",
        r"dime",
        r"quiero saber",
        r"el precio",
        r"precio",
        r"valor",
        r"stock",
        r"de una acci[oó]n",
        r"de la acci[oó]n",
        r"acci[oó]n",
        r"de",
        r"la",
        r"el",
    ]

    for expresion in expresiones:
        texto = re.sub(rf"\b{expresion}\b", " ", texto)

    # Eliminar espacios repetidos
    texto = re.sub(r"\s+", " ", texto).strip()

    return texto
