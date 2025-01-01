import jwt
import time

private_key = """-----BEGIN PRIVATE KEY-----<PRIVATE_KEY>-----END PRIVATE KEY-----"""

payload = {
    "iss": "<ISSUER>",
    "scope": "<SCOPE>",
    "aud": "<AUDIENCE>",
    "iat": int(time.time()),
    "exp": int(time.time()) + 3600 # Expires in 1 hour
}

token = jwt.encode(payload, private_key, algorithm="RS256") # Doesn't have to be RS256
print(token)