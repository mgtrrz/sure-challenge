# sure challenge

## Running the script

Run `docker-compose up --build` to start up localstack with S3 running, an init script that will create the bucket and some random objects that resemble deployments with assets.

To run the main.py script, wait a few moments for the init script to finish creating objects, then in a new terminal run:
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```


The script also takes an argument for how many recent deployments to keep:
```
python3 main.py 8
```

otherwise, it assumes the most recent 5.