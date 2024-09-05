import tweepy
import os

# Credenciales de Twitter desde los secrets en GitHub
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

print("Iniciando autenticación con Twitter...")

# Autenticación con la API de Twitter usando Tweepy
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

print("Autenticación completada. Obteniendo menciones...")

# Obtener las últimas 5 menciones
mentions = api.mentions_timeline(count=5)

print(f"Se encontraron {len(mentions)} menciones.")

# Responder a cada mención con un toque ingenioso
for mention in mentions:
    user_name = mention.user.screen_name
    mention_text = mention.text
    print(f"Procesando mención de {user_name}: {mention_text}")
    tweet_response = process_tweet(mention_text, user_name)
    
    # Publicar la respuesta en Twitter
    api.update_status(tweet_response, in_reply_to_status_id=mention.id)
    print(f"Respuesta enviada a {user_name}: {tweet_response}")

print("Finalización del script.")
