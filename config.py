from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "12987003"))
API_HASH = getenv("API_HASH", "8eeec246fa88a87d89a1bc2bca56345f")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","🦋⃟ᴠͥɪͣᴘͫ✮⃝🇲iss 🇶𝖚𝖊𝖊𝖓𝄟⃝")
BOT_USERNAME = getenv("BOT_USERNAME", "QUEEN_MUSIQ_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "AANDAVAR8064")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Immissqueen")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500"))
START_IMG = getenv("START_IMG", "https://telegra.ph//file/081329fa4817b83ad37c8.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/fe7570d1c6910be53533c.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5065752827").split()))
