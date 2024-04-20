import boto3
import os
import random
import uuid
from time import sleep

BUCKET_NAME = "s3-bucket-name"
ENDPOINT_URL = os.environ["ENDPOINT_URL"] if "ENDPOINT_URL" in os.environ else "http://localhost:4566"

def main():
    # initialize a bucket with objects for this demo
    client = boto3.client("s3", endpoint_url=ENDPOINT_URL)
    client.create_bucket(Bucket=BUCKET_NAME)

    for x in range(10):
        # Generate x directories/objects with a random string/hash
        # And sleep to put some time in between objects
        sleep(random.randrange(1, 3))
        k = uuid.uuid4().hex[:8]
        client.put_object(Bucket=BUCKET_NAME, Key=f"{k}/index.html")
        client.put_object(Bucket=BUCKET_NAME, Key=f"{k}/style.css")

    # List the objects we've created 
    results = client.list_objects_v2(Bucket=BUCKET_NAME)["Contents"]
    print("Done! Objects created:")
    for obj in results:
        print(f"{obj['Key']} {obj['LastModified'].isoformat()}")


if __name__ == '__main__':
    main()