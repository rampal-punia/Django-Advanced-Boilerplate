'''script to generate a secret token of length 50'''

import secrets
print(secrets.token_hex(25))
