## Info:
Script send message ("/bridges") to @GetBridgesBot and set obfs4 proxy in torrc


## Setup:

`git clone https://github.com/delyee/getOnionBridgeFromTelegram`

1. `pip3 install -r requirements.txt`
2. Create app - https://my.telegram.org/apps
3. Get "api_id" & "api_hash" and paste in config.py
4. Paste your phone number in config.py
5. `apt install tor obfs4proxy`
6. `echo "ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy" >> /etc/tor/torrc`
7. `echo "UseBridges 1" >> /etc/tor/torrc`
8. `python3 main.py`

**!** First start: paste 6-digit code from Telegram notification in console & press `Enter`

Congratulations, you are beautiful. Logs in `getbridges.log`

## Cron
`crontab -e` and paste `@reboot sleep 60 && /usr/bin/python3 /root/getOnionBridgeFromTelegram-master/main.py`

## systemd

1. `cp getOnionBridgeFromTelegram-master/systemd/*`
2. `systemctl daemon-reload && systemctl disable getonionbridges.service && systemctl enable getonionbridges.timer`

status: `systemctl status getonionbridges.timer`



