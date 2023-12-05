from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 28215977))
    API_HASH = env.get("TELEGRAM_API_HASH", "393c7aacd1e36d9143524bd5d1ccb866")
    OWNER_ID = int(env.get("OWNER_ID", 835553455))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "INDEXOK2BOT_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6575111861:AAFSPd8skKv-0i1BeLaLS_wCQmEa68B7Z8M")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001846664363))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://filestreambothelp-2a47363e2cd7.herokuapp.com")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", ))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
