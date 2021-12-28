## Info:
Script send "/bridges" to @GetBridgesBot, set obfs4 proxy in torrc and restart tor


## Setup:

`git clone https://github.com/delyee/getOnionBridgeFromTelegram`

1. `pip3 install -r requirements.txt`
2. Create app - https://my.telegram.org/apps & get "api_id" / "api_hash"
3. Paste your phone number, api_id and api_hash in config.py
4. `apt install tor obfs4proxy`
5. `echo "ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy" >> /etc/tor/torrc`
6. `echo "UseBridges 1" >> /etc/tor/torrc`
7. `python3 main.py`

**[!]** First start: paste 6-digit code from Telegram notification in console & press `Enter`

Congratulations, you are beautiful. Logs in `getbridges.log`


## supervisord

1. `python3 main.py` and paste 6-digit code from Telegram
2. `cp getOnionBridgeFromTelegram/conf/supervisord/getOnionBridgeFromTelegram.conf /etc/supervisor/conf.d/`
3. change work directory (line 4) and timeout (line 5) in `/etc/supervisor/conf.d/getOnionBridgeFromTelegram.conf`
4. `systemctl reload supervisord`

check status: `supervisorctl status getOnionBridgeFromTelegram`


## Cron
1. `python3 main.py` and paste 6-digit code from Telegram
2. `crontab -e`
3. `@reboot sleep 60 && /usr/bin/python3 /root/getOnionBridgeFromTelegram/main.py`

## systemd

1. `python3 main.py` and paste 6-digit code from Telegram
2. change path in `getOnionBridgeFromTelegram/conf/systemd/getonionbridges.service`
3. `python3 main.py` and paste 6-digit code from Telegram
4. Copy `getOnionBridgeFromTelegram/conf/systemd/*`
5. `systemctl daemon-reload && systemctl disable getonionbridges.service && systemctl enable getonionbridges.timer`

check status: `systemctl status getonionbridges.timer`



