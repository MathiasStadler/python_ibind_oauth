# FROM HERE
# https://github.com/Voyz/ibind/blob/master/examples/rest_08_oauth.py

"""
REST basic.

Minimal example of using the IbkrClient class.
"""

from ibind import IbkrClient

client = IbkrClient(
    use_oauth=True,
    oauth_config=OAuth1aConfig(
        access_token='my_access_token',
        access_token_secret='my_access_token_secret',
        consumer_key='my_consumer_key',
        dh_prime='my_dh_prime',
        encryption_key_fp='my_encryption_key_fp',
        signature_key_fp='my_signature_key_fp',
    )
)

# Construct the client
client = IbkrClient()

# Call some endpoints
print('\n#### check_health ####')
print(client.check_health())

print('\n\n#### tickle ####')
print(client.tickle().data)

print('\n\n#### get_accounts ####')
print(client.portfolio_accounts().data)
