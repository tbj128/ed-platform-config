# ed-platform-config

```
openssl genrsa -out /path_to_key/privatekey.pem 2048
openssl req -new -x509 -key /path_to_key/privatekey.pem -out /path_to_key/publickey.pub.pem -subj '/CN=myapp'
python3 generate_jwk.py
```
