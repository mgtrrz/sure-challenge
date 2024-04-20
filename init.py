import boto3
import uuid
import random
from time import sleep

max_deployments = 5
bucket_name = "s3-bucket-name"
endpoint_url = "http://localstack:4566"

def main():
    # initialize a bucket with objects for this demo
    client = boto3.client("s3", endpoint_url=endpoint_url)
    client.create_bucket(Bucket=bucket_name)

    for x in range(10):
        # Generate x directories/objects with a random string/hash
        # And sleep to put some time in between objects
        sleep(random.randrange(1, 3))
        k = uuid.uuid4().hex[:8]
        client.put_object(Bucket=bucket_name, Key=f"{k}/index.html")
        client.put_object(Bucket=bucket_name, Key=f"{k}/style.css")

    # List the objects we've created 
    results = client.list_objects_v2(Bucket=bucket_name)["Contents"]
    print("Objects created:")
    for obj in results:
        print(f"{obj['Key']} {obj['LastModified'].isoformat()}")


if __name__ == '__main__':
    main()