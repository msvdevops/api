#!/usr/bin/env python3

import connexion

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'This is a nokia innovation platform Apis. '})
    app.run(port=8080, host="0.0.0.0")
