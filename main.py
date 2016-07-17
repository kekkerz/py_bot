from src.bot import *
from src.config.config import *
import sys

try:
	bot = twitch_bot(config).start() #Begin bot

except KeyboardInterrupt:
	sys.exit()
