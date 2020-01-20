## Rui with virtualenv

```
pip install virtualenv
virtualenv env
source env/bin/activate
```

## Dependencies

```
env/bin/pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib genanki google-cloud-texttospeech
```

## Env variables
Method used for passing secrets to the script
- `GOOGLE_APPLICATION_CREDENTIALS`: Google service account json private key used for text-to-speech GCloud API.
- `ANKI_MEDIA_DIR`: Anki media library location, usually `Library/Application\ Support/Anki2/User\ 1/collection.media/`