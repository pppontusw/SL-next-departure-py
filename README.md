# SL Next Departure

## Compatibility

Python 3.5.x

## Instructions

Clone the repo and create a config.py in the root with the following content:

```
import os
import uuid
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = str(uuid.uuid4())
SL_HPL2_KEY = 'Your key for the station data API'
SL_R3_KEY = 'Your key for the Realtime data API'

```

Make a virtualenv and install requirements

```
pontus$ virtualenv -p python3 . 
pontus$ source bin/activate
pontus$ pip install -r requirements.txt
```

Run the application

```
pontus$ ./run.py 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```