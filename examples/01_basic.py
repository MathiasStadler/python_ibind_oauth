# FROM HERE
# https://github.com/Voyz/ibind/blob/master/examples/rest_08_oauth.py

"""
REST basic.

Minimal example of using the IbkrClient class.
"""

from ibind import IbkrClient

# client = IbkrClient(
#     use_oauth=True,
#     oauth_config=OAuth1aConfig( # noqa: F821
#         access_token='my_access_token',
#         access_token_secret='my_access_token_secret',
#         consumer_key='my_consumer_key',
#         dh_prime='my_dh_prime',
#         encryption_key_fp='my_encryption_key_fp',
#         signature_key_fp='my_signature_key_fp',
#     )
# )

client = IbkrClient(
    use_oauth=True,
    oauth_config=OAuth1aConfig( # noqa: F821
        access_token='9d17a4c92a93c6daa562',
        access_token_secret='p4E4FLQr8K81bERvUKk7ZmViBKMZEEO6PYPEeMlJbTh1BWo1tTaHODcN8V4A8UIRfZKcdTNTGa3gZEpIfU2kfKjPtHJKlxikR3PEDBTAanMa9plKuUleUsBjaqQ3Gnf/78a3ppP7QfO30SA9GFG0oxkHEXPdS4iP4mVtyl5PKDptS4NVem6mB9Iylu8x9tzae/iz1lIIDed/erIBdhDOovTo4oDamljnr8o+hQXyc53YqInvyAEQude1tdwlKpNJZTPQ+N/96fcpBN75Lffr+0Te/H/+GAWDYr7w1QeXvmPgGCT0M9QkKQhwu/fg1mio57BjfhV7GXvBKJOWvUmYWA==',
        consumer_key='YXCVBNMQW',
        dh_prime='MIIBDAKCAQEAsdTPVxxyxmMvEc9OUbhr0464ejV/LbuteTwGZvReUl74Hy+2pZhwd4rAm513dUH4lM/qygOb2NTGNKqFUUlb3ObMu2Mzab54HBrD9bBeGcnBbBOXPmsgVSvZAoCJI2voJjtqO1LX6Jqt9T5LIEiCR8Xp3+HDO12P100cmcrvUYDL+Me3q7YUpuzbE4aXxpZe8S2CY9BAyhr0oReZ5MUniyJkLcbX4Yi2JVdmnErWPTnSY+6VnaGJDRJmP+e1oNh0veW2mjeZexIVR3nr5OxJiY+3hJtvdmhv6B5yVbb38oA7fsYuSALgfXRtXUCtSGZTqCqlF5C7fJiGMAH8ipd89wIBAgICAOE=',
        encryption_key_fp='MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5uaTIzPnDJ6oKzePrblzrQFXm/sF039xFe0+qotLmF9/U1Quv48jhhQ3yaLefjGAgURnzHFX6jJlPeFh9nE8VgwM53YnqQz41MbTc0a1iJtzsAOnAqs1ZSxf3JoYTRaPizlUZraZ33R6KT6md5gpLzM4XdpqB5v4NKN83L28hSTqGhqJcFb6mpFAm9wFvo9I7yHWCroqzLQBNwWXIvs41xegWi5h6lbQ4UIkVpTx+KBqbH5WnmXAXkDhWUhaQoGJBJsfBKRovrfZZkY4xvbcd1PWvnvDv5VJS0OWmoSyw/xVv9htlD2vsKKB2qfMS/1ub5eh7orXjE5cjvc2BP6JuQIDAQAB',
        signature_key_fp='MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0Tc7ltdeeMVhfYtSHAfpnpOwvR1bvFWRug/r8/ArroUxuv8jexsDtLauiAOEg5/dbWs6Hz2v7RovcjpBuiE1ezMAL8Yju/SG5q77Pz1X4zxWGznsA8h1XitjvtFnQo0dB/ohaVidlib5aLT4B+mWC9LY96cf34wFgsWwINI2+MCd9u3AWGiJ4SqJnvDBYzbhGzI38TD7aD4QqXABC7sQD6fmEHmTlf6Iaz0g4QpKGRCOCV4L3NkRKgBrIyPYzrQ8jVGeSU8SWnpzWe61EfnJfE3VUTPtZjvVWMVlg8g5QdqltROm0jHTZMjBZxY2YAw1p63Ms79bGTUcFUKshsPQEQIDAQAB',
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
