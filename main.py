from telethon import TelegramClient, sync, errors
import logging
from config import *
from os import system
from time import sleep
from sys import argv

#os.chdir(os.path.dirname(os.path.realpath(__file__))) # hack for systemd

logger = logging.getLogger("getbridges")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("getbridges.log") # TODO: auto-rotation
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

client = TelegramClient('poster', api_id, api_hash)
client.start(phone=phone_number)

def main():
	client.send_message("@GetBridgesBot", "/bridges")
	entity=client.get_entity("GetBridgesBot")

	for message in client.iter_messages(entity, from_user=entity):
		BRIDGE = message.text # last message

	logger.info(BRIDGE)

	with open('/etc/tor/torrc') as f:
		LINES = f.readlines()

	OUTPUT_LINES = []

	found = False
	for line in LINES:
		if 'bridge obfs4' in line:
			found = True
			OUTPUT_LINES.append("bridge {}\n".format(BRIDGE))
		else:
			OUTPUT_LINES.append(line)

	if found:
		pass
	else:
		OUTPUT_LINES.append("bridge {}\n".format(BRIDGE))

	with open('/etc/tor/torrc', 'w') as f:
		f.writelines(OUTPUT_LINES)

	system("systemctl restart tor")
	logger.info("tor restarting...")


# section for supervisord
if len(argv) > 0:
	while True:
		main()
		try:
			sleep(int(argv[1]))
		except ValueError:
			logger.critical("Timeout value is invalid - {}, set default - 10800".format(argv[1]))
			sleep(10800)
else:
	main()

# kill me for this code .__.