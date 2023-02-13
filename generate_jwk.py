import jwcrypto.jwk as jwk
import json

with open("physiohub.pub.pem", "rb") as pemfile:
    key = jwk.JWK.from_pem(pemfile.read())

    data = {
        "keys": [
            json.loads(key.export_public())
        ]
    }

    with open('physiohub.pub.jwks', 'w') as f:
        json.dump(data, f)
