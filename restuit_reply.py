import tweepy
import os

# Credenciales de Twitter desde los secrets en GitHub (estas se deben almacenar como variables de entorno o usarlas directamente si no usas secrets)
consumer_key = 'tYEkW50YVJh767fIZjcFUy7iD'
consumer_secret = '3ABDOkjqWjFQCYzvNbZ9FtelSGfwPYS85XKR9gpfFj3HRtEaRC'
access_token = '1445541467175337994-vH5ctinZJMkB4Nqsv4uTHNfx82DH4N'
access_token_secret = 'jwLL8WrleRoo8IPSlDOqslDW2UJhsj5bEIWpSj7yT1HCi'

# Autenticación con la API de Twitter usando Tweepy
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Aquí procesaremos el tweet para generar la respuesta
def process_tweet(mention_text, user_name):
    response = ""
    if "brillante" in mention_text.lower():
        response = f"@{user_name} ¡Oh, gracias por iluminarme con tu sabiduría brillante! #Ironía"
    elif "genio" in mention_text.lower():
        response = f"@{user_name} ¡Qué humilde eres, me haces sentir tan pequeño! #Sarcasmo"
    else:
        response = f"@{user_name} ¡Gracias por la mención! Ahora cuéntame algo más interesante. #OJO"
    
    return response

# Simulamos que recibimos una mención de Twitter (esto lo recibirás desde IFTTT)
mention_text = os.getenv('MENTION_TEXT')  # Texto del tweet enviado desde IFTTT
user_name = os.getenv('MENTION_USER')  # Nombre de usuario del que te mencionó

# Generar la respuesta según la mención
tweet_response = process_tweet(mention_text, user_name)

# Enviar la respuesta a Twitter
api.update_status(tweet_response)
