# Reto #30: El teclado T9
#### Dificultad: Media | Publicación: 24/07/23 | Corrección: 31/07/23

## Enunciado
#
# Los primeros dispositivos móviles tenían un teclado llamado T9
# con el que se podía escribir texto utilizando únicamente su
# teclado numérico (del 0 al 9).
#
# Crea una función que transforme las pulsaciones del T9 a su
# representación con letras.
# - Debes buscar cuál era su correspondencia original.
# - Cada bloque de pulsaciones va separado por un guión.
# - Si un bloque tiene más de un número, debe ser siempre el mismo.
# - Ejemplo:
#     Entrada: 6-666-88-777-33-3-33-888
#     Salida: MOUREDEV
#


# Para transformar las pulsaciones del teclado T9 a su representación con letras, necesitaremos crear una función que mapee cada número 
# del 0 al 9 a su respectiva letra.
# Esta función toma la entrada en formato T9 y la divide en bloques separados por guiones. Luego, cada bloque se mapea a su representación 
# de letras de acuerdo con el teclado T9, siguiendo las reglas que mencionaste. La función finalmente devuelve el texto resultante.

def t9_to_text(t9_input):
    t9_mapping = {
        '2': 'ABC', '3': 'DEF', '4': 'GHI',
        '5': 'JKL', '6': 'MNO', '7': 'PQRS',
        '8': 'TUV', '9': 'WXYZ'
    }

    t9_input = t9_input.split('-')
    result = ''

    for block in t9_input:
        if len(block) == 1:
            result += t9_mapping[block][0]
        else:
            char = t9_mapping[block[0]][len(block) - 1]
            result += char

    return result

# Ejemplo de uso
entrada = "6-666-88-777-33-3-33-888"
salida = t9_to_text(entrada)
print(salida)  # Salida: MOUREDEV
