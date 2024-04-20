import boto3
import os
import sys
from time import sleep

MAX_DEPLOYMENTS = 5
BUCKET_NAME = "s3-bucket-name"
ENDPOINT_URL = os.environ["ENDPOINT_URL"] if "ENDPOINT_URL" in os.environ else "http://localhost:4566"

get_last_modified = lambda obj: obj["LastModified"]

def main():
    # The actual script wouldn't have this but we need to wait for the init script to finish creating objects
    # if everything came up by docker-compose.
    if "DOCKER_COMPOSE" in os.environ: sleep(20)

    # Check for how many recent deployments to keep
    args = sys.argv[1:]
    if len(args) > 0:
        MAX_DEPLOYMENTS = args[0]
    elif "MAX_DEPLOYMENTS" in os.environ:
        MAX_DEPLOYMENTS = os.environ["MAX_DEPLOYMENTS"]

    client = boto3.client("s3", endpoint_url=ENDPOINT_URL)
    results = client.list_objects_v2(Bucket=BUCKET_NAME)["Contents"]

    # Reverse sort by most recent the objects in our bucket
    results_sorted = [obj for obj in sorted(results, key=get_last_modified, reverse=True)]

    print("Older objects deleted:")
    for obj in results_sorted:
        print(f"{obj['Key']} {obj['LastModified'].isoformat()}")


if __name__ == '__main__':
    main()