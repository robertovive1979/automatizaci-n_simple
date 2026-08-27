# Módulo encargado de la integración con servicios meteorológicos externos
import re
import requests


def obtener_clima(driver, user_input):
    """
    Obtiene la temperatura actual de una ciudad utilizando el servicio wttr.in.

    Argumentos:
        driver: Instancia de Selenium WebDriver (se mantiene por compatibilidad).
        user_input: Texto ingresado por el usuario.

    Retorna:
        Una cadena con la temperatura actual o un mensaje de error.
    """

    # Convertir la entrada a minúsculas y eliminar signos de puntuación
    city = user_input.lower().strip()
    city = re.sub(r"[¿?¡!,.;:]", "", city)

    # Eliminar expresiones relacionadas con la consulta del clima
    patrones = [
        r"cu[aá]l es",
        r"cu[aá]nto hace",
        r"dime",
        r"quiero saber",
        r"la temperatura actual",
        r"temperatura actual",
        r"la temperatura",
        r"temperatura",
        r"el clima",
        r"clima",
        r"el tiempo",
        r"tiempo",
    ]

    for patron in patrones:
        city = re.sub(rf"\b{patron}\b", " ", city)

    # Eliminar "en" y "de" solamente cuando son palabras completas
    city = re.sub(r"\b(?:en|de)\b", " ", city)

    # Eliminar espacios repetidos
    city = re.sub(r"\s+", " ", city).strip()

    # Verificar que se haya identificado una ciudad
    if not city:
        return "No se pudo identificar la ciudad."

    try:
        # Consultar la temperatura actual en wttr.in
        response = requests.get(
            f"https://wttr.in/{city}",
            params={"format": "%t"},
            timeout=10
        )

        if response.status_code == 200:
            temperatura = response.text.strip()
            return temperatura

        return "No se pudo obtener el clima para esa ubicación."

    except requests.RequestException as e:
        return f"Error de red al obtener el clima: {e}"
