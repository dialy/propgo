from telethon import TelegramClient, events
import os
import logging

# Configuration du logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration depuis les variables d'environnement
API_ID = os.environ['API_ID']
API_HASH = os.environ['API_HASH']
PHONE_NUMBER = os.environ['PHONE_NUMBER']
TARGET_USER = os.environ['TARGET_USER']

# Paramètres spécifiques
TARGET_GROUP = 'tforwin'
KEYWORD = 'PROP GO'
MESSAGE_TO_SEND = 'gagner la prop firm SVP'

# Créer le client
client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(chats=TARGET_GROUP))
async def handler(event):
    try:
        if KEYWORD.lower() in event.text.lower():
            logger.info(f"Mot-clé '{KEYWORD}' détecté")
            await client.send_message(TARGET_USER, MESSAGE_TO_SEND)
            logger.info(f"Message envoyé à {TARGET_USER}")
    except Exception as e:
        logger.error(f"Erreur : {e}")

async def main():
    await client.start(phone=PHONE_NUMBER)
    logger.info("Bot démarré")
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    client.loop.run_until_complete(main())
