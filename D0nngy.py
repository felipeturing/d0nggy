# Como jugando, por ahora.
from requests_oauthlib import OAuth1Session
import os
import json

# consumer_key & consumer_secret: As the username and password that represents the D0nggy App when making API requests.
consumer_key = os.environ.get("CONSUMER_KEY_D0NGGY")
consumer_secret = os.environ.get("CONSUMER_SECRET_D0NGGY")

# access_token & access_token_secret: An Access Token and Secret are user-specific credentials used to authenticate OAuth 1.0a API requests. They specify the Twitter account the request is made on behalf of.
access_token = os.environ.get("ACCESS_TOKEN_D0NGGY") 
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET_D0NGGY")

# Get request token
# request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
# oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

# try:
#     fetch_response = oauth.fetch_request_token(request_token_url)
# except ValueError:
#     print(
#         "Hay problemas con los consumer_key o consumer_secret"
#     )

# resource_owner_key = fetch_response.get("oauth_token")
# resource_owner_secret = fetch_response.get("oauth_token_secret")
# print("El token OAuth es: %s" % resource_owner_key)

# # Get authorization
# base_authorization_url = "https://api.twitter.com/oauth/authorize"
# authorization_url = oauth.authorization_url(base_authorization_url)
# print("Please go here and authorize: %s" % authorization_url)
# verifier = input("Paste the PIN here: ")

# # Get the access token
# access_token_url = "https://api.twitter.com/oauth/access_token"
# oauth = OAuth1Session(
#     consumer_key,
#     client_secret=consumer_secret,
#     resource_owner_key=resource_owner_key,
#     resource_owner_secret=resource_owner_secret,
#     verifier=verifier,
# )
# oauth_tokens = oauth.fetch_access_token(access_token_url)

# access_token = oauth_tokens["oauth_token"]
# access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
# oauth = OAuth1Session(
#     consumer_key,
#     client_secret=consumer_secret,
#     resource_owner_key=access_token,
#     resource_owner_secret=access_token_secret,
# )

"""
consumer_key & consumer_secret: As the username and password that represents the D0nggy App when making API requests.

access_token & access_token_secret: They specify the Twitter account the request is made on behalf of.
"""
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

tuit = "🎶 Tu vida y mi vida\nHan nacido para estar unidas\nAlmas de fuego\nMuévete un poquito más\nMuévete un poquito más\nMuévete un poquito más, más.🎶"
payload = {"text": tuit}

response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

if response.status_code != 201:
    raise Exception(
        "Ocurrió un error en la petición POST: {} {}".format(response.status_code, response.text)
    )

print("Código de respuesta: {}".format(response.status_code))

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
