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

# Procesar la mención y generar una respuesta ingeniosa
def process_tweet(mention_text, user_name):
    if "brillante" in mention_text.lower():
        response = f"@{user_name} Oh, claro, soy tan brillante que necesito gafas de sol para verme. #Ironía"
    elif "genio" in mention_text.lower():
        response = f"@{user_name} Si fuera un genio, ya habría pedido tres deseos... ¿tienes alguno tú? #Sarcasmo"
    elif "gracias" in mention_text.lower():
        response = f"@{user_name} ¡Oh, no me agradezcas, que después me malacostumbro! #OJO"
    else:
        response = f"@{user_name} Interesante, pero creo que aún puedo escuchar los grillos... cuéntame algo más jugoso. #Ingenio"
    return response

# Obtener las últimas 5 menciones
mentions = api.mentions_timeline(count=5)

# Responder a cada mención con un toque ingenioso
for mention in mentions:
    user_name = mention.user.screen_name
    mention_text = mention.text
    tweet_response = process_tweet(mention_text, user_name)
    
    # Publicar la respuesta en Twitter
    api.update_status(tweet_response, in_reply_to_status_id=mention.id)
