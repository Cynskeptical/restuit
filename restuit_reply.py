import tweepy
import os

# Credenciales de Twitter desde los secrets en GitHub
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Agrega mensajes para verificar las credenciales
print("Iniciando el proceso de autenticación...")
print(f"Consumer Key: {consumer_key}")
print(f"Consumer Secret: {consumer_secret[:5]}...")  # No mostrar la clave completa por seguridad
print(f"Access Token: {access_token[:5]}...")
print(f"Access Token Secret: {access_token_secret[:5]}...")

# Autenticación con la API de Twitter usando Tweepy
try:
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    print("Autenticación completada con éxito.")
except Exception as e:
    print(f"Error durante la autenticación: {e}")
    exit(1)

# Obtener las últimas 5 menciones
print("Obteniendo las últimas 5 menciones...")
try:
    mentions = api.mentions_timeline(count=5)
    print(f"Se encontraron {len(mentions)} menciones.")
except Exception as e:
    print(f"Error al obtener menciones: {e}")
    exit(1)

# Responder a cada mención con un toque ingenioso
for mention in mentions:
    user_name = mention.user.screen_name
    mention_text = mention.text
    print(f"Procesando mención de {user_name}: {mention_text}")
    
    # Procesar la mención y generar una respuesta ingeniosa
    tweet_response = process_tweet(mention_text, user_name)
    print(f"Respuesta generada: {tweet_response}")
    
    # Publicar la respuesta en Twitter
    try:
        api.update_status(tweet_response, in_reply_to_status_id=mention.id)
        print(f"Respuesta enviada a {user_name}: {tweet_response}")
    except Exception as e:
        print(f"Error al enviar la respuesta: {e}")
        continue

print("Script finalizado con éxito.")
