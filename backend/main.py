import os
from website import create_app
import configparser

config = configparser.RawConfigParser()
config.read('serverconf.cfg')

app = create_app()

if __name__ == '__main__':

   if config.get('SERVER', 'modus') == 'dev':
      app.run(debug = True, port = config.get('SERVER', 'port'))
      print("Server was startet in development")

   elif config.get('SERVER', 'modus') == 'prod':
      from waitress import serve
      serve(app, host = config.get('SERVER', 'ip'), port=config.get('SERVER', 'port'))
      print("Server was startet in development")

   
   else:
      print('unknown server modus, check serverconf file')