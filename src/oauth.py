from rauth import OAuth2Service
from src.app import app


vk = OAuth2Service(
    name='vk',
    client_id=app.config['OAUTH_CREDENTIAL']['id'],
    client_secret=app.config['OAUTH_CREDENTIAL']['secret'],
    authorize_url="https://oauth.vk.com/authorize",
    access_token_url="https://oauth.vk.com/access_token",
    base_url="https://api.vk.com/method/"
)
