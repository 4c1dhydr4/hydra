#!/bin/sh

# Provides: superscript
# Required-Start:
# Required-Stop:
# Default-Start:
# Default-Stop:
# Short-Description:	launcher for blackhydra__
# Description:	BlackHydra launcher
### END INIT INFO

#cd /
cd /home/pi/hydra/
#python3 lcd_start.py > /home/pi/blackhydra/logs/lcd_log &
#python3 telegram_bot.py > /home/pi/blackhydra/logs/telegram_log &
#python3 alerts_script.py > /home/pi/blackhydra/logs/alerts_script_log &
python3 manage.py runserver 0.0.0.0:8080 > /home/pi/hydra/logs/django.log &
python3 main.py > /home/pi/hydra/logs/hydra.log &
cd /

