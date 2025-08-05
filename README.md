# 🗣️ Tanglish API

A simple Flask API that converts Tamil text into Tanglish (Romanized Tamil) using the `indic-transliteration` library.

### Endpoint:
`POST /tanglish`

### Request:
```json
{ "text": "நீங்கள் எப்படி இருக்கிறீர்கள்?" }
```

### Response:
```json
{ "tanglish": "nIngaL eppaTi irukkiRIRkaL?" }
```

### Deployment:
Ready for platforms like Render.com, Railway.app, etc.