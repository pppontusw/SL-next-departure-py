# SL Next Departure

Create config.py

```
import os
import uuid
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = str(uuid.uuid4())
SL_HPL2_KEY = 'Your key for the station data API'
SL_R3_KEY = 'Your key for the Realtime data API'

```