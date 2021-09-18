import os
from website import create_app
import serverconf as cfg

app = create_app()

if __name__ == '__main__':

   if cfg.server['modus'] == 'dev':
      app.run(debug = True, port = cfg.server['port'])

   elif cfg.server['modus'] == 'prod':
      from waitress import serve
      serve(app, host = cfg.server['ip'], port=cfg.server['port'])
   
   else:
      print('unknown server modus, check serverconf file')