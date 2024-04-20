# sure challenge

## Running the script

Run `docker-compose up --build` to start up localstack with S3 running and an init script that will create the bucket and some random objects that resemble deployments with assets.

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

Otherwise, it assumes the most recent 5. The scripts also take in environment variables assuming it wil run in a container. An ideal location for this script to run may be in a serverless setting.

If you have [awslocal installed](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal), add new items with:

```
hash=$(openssl rand -base64 8 | tr -dc A-Za-z0-9); awslocal s3api put-object --bucket s3-bucket-name --key "${hash}/index.html"; awslocal s3api put-object --bucket s3-bucket-name --key "${hash}/css/font.css"; awslocal s3api put-object --bucket s3-bucket-name --key "${hash}/images/hey.png"
```

Alternatively, you can re-run the init script locally `python3 init.py`.

If you re-run the main.py script, you'll see it deleting older items, keeping the most recent 5 deployments.

Point it to a real bucket by exporting environment variables `BUCKET_NAME` and `ENDPOINT_URL`.

## Assumptions

- This script assumes the name of the bucket is "s3-bucket-name". You can change the name of the bucket by setting the environment variable `BUCKET_NAME`.
- This script assumes that we're talking to and authenticating with localstack. This script may either be adapted to remove these assumptions and use the default endpoint or you can set environment variable `ENDPOINT_URL` to point to AWS' S3 API, such as `https://s3.us-east-1.amazonaws.com`.
- This script assumes that the deployments go by the last modified date of the objects and that these objects won't be modified after they've been uploaded to S3.
- This script also assumes that the deployment name (the hash) does not contain any symbols such as `/`.
- This script assumes that conditions are ideal and does not do any proper error handling, such as checking to see if the bucket exists or is accessible. Before deploying this to production, we'd want to add more error handling.
- This script assumes that each deployment only has a few files and does not properly paginate items. If this were in production, we'd properly want to make sure we paginate all the items in a bucket in case it exceeds the default limit that `list_objects_v2` returns.