import re

from funciones_agente.obtener_precio_accion import obtener_precio_accion
from funciones_agente.obtener_clima import obtener_clima


def chatbot():
    """
    Función principal del chatbot.

    El chatbot reconoce consultas relacionadas con:
    - Precio de acciones
    - Clima o temperatura
    - Comandos para salir
    """

    print("*** Chatbot v1.0.0 ***")
    print("Hola, soy el Chatbot v1.0.0.")
    print("Puedo ayudarte a consultar precios de acciones y la temperatura actual.")
    print()
    print("Ejemplos:")
    print("  ¿Cuál es el precio de una acción de Microsoft?")
    print("  ¿Cuál es la temperatura actual en Guadalajara?")
    print()
    print("Escribe 'salir' para terminar.\n")

    while True:
        try:
            # Leer la consulta del usuario
            user_input = input("--> ").strip()

            # Ignorar entradas vacías
            if not user_input:
                continue

            # Comando para finalizar el chatbot
            if user_input.lower() in [
                "salir",
                "exit",
                "quit",
                "adiós",
                "adios"
            ]:
                print(">>> ¡Hasta luego!")
                break

            # Detectar intención relacionada con acciones
            stock_intent = re.search(
                r"\b(precio|valor|cotización|cotizacion|stock|acción|accion)\b",
                user_input,
                re.IGNORECASE
            )

            # Detectar intención relacionada con clima
            weather_intent = re.search(
                r"\b(clima|temperatura|tiempo)\b",
                user_input,
                re.IGNORECASE
            )

            # Consulta de precio de acciones
            if stock_intent:
                resultado = obtener_precio_accion(None, user_input)

                if resultado:
                    print(f">>> {resultado}")
                else:
                    print(">>> No pude obtener el precio de esa acción.")

            # Consulta de clima
            elif weather_intent:
                resultado = obtener_clima(None, user_input)

                if resultado:
                    print(f">>> {resultado}")
                else:
                    print(">>> No pude obtener la temperatura de esa ciudad.")

            # Consulta no reconocida
            else:
                print(
                    ">>> No estoy seguro de cómo ayudarte con eso. "
                    "Puedes preguntarme por el precio de una acción "
                    "o por la temperatura de una ciudad."
                )

        except KeyboardInterrupt:
            print("\n>>> ¡Hasta luego!")
            break

        except Exception as e:
            print(f">>> Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    chatbot()
