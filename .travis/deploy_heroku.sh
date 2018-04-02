#!/bin/sh
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku plugins:install heroku-container-registry
echo "$HEROKU_API_KEY" | docker login -u "$HEROKU_EMAIL" --password-stdin registry.heroku.com
heroku container:push web --app $HEROKU_APP_NAME
