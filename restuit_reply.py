import os

# Aquí procesaremos el tweet para generar la respuesta
def process_tweet(mention_text):
    response = ""
    if "brillante" in mention_text:
        response = "¡Oh, gracias por iluminarme con tu sabiduría brillante! #Ironía"
    elif "genio" in mention_text:
        response = "¡Qué humilde eres, me haces sentir tan pequeño! #Sarcasmo"
    else:
        response = "¡Gracias por la mención! Ahora cuéntame algo más interesante. #OJO"
    
    return response

# Simulamos que recibimos una mención de Twitter
mention_text = "Eres tan brillante"
response = process_tweet(mention_text)
print(response)
