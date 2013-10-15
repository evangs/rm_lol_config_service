rm_lol_config_service
=====================
For some reason league of legends crashes on my system after each game.  To resolve the issue I need to delete the leage of legends game config.  Each time the game runs it rebuilds the config, so after every game I have to delete it.  I wrote a script that I could run after each game, but I forget and am lazy so I converted it into a service that always runs and takes care of deleting the config for me.

active python is required for this service to work http://www.activestate.com/activepython/downloads



installation
============
python rm_lol_config_service.py install
