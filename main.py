import boto3
import os
import sys

args = sys.argv[1:]
# Check for how many recent deployments to keep
if len(args) > 0:
    MAX_DEPLOYMENTS = int(args[0])
elif "MAX_DEPLOYMENTS" in os.environ:
    MAX_DEPLOYMENTS = os.environ["MAX_DEPLOYMENTS"]
else:
    MAX_DEPLOYMENTS = 5

BUCKET_NAME = "s3-bucket-name"
ENDPOINT_URL = os.environ["ENDPOINT_URL"] if "ENDPOINT_URL" in os.environ else "http://localhost:4566"

# Returns an anonymous function for retrieving the LastModified key in the S3 objects list.
get_last_modified = lambda obj: obj["LastModified"]

def main():
    client = boto3.client("s3", endpoint_url=ENDPOINT_URL)
    results = client.list_objects_v2(Bucket=BUCKET_NAME)["Contents"]

    # Reverse sort by most recent objects (order by LastModified datetime object) in our bucket
    results_sorted = [obj for obj in sorted(results, key=get_last_modified, reverse=True)]

    print(f"Current objects:")
    for obj in results_sorted:
        print(f"{obj['Key']}\t{obj['LastModified'].isoformat()}")

    # Just get the directory name and remove duplicates, preserving the list order
    sorted_keys = list(dict.fromkeys([obj["Key"].split("/")[0] for obj in results_sorted]))

    # Make a list of the deployment "directories" that exceed MAX_DEPLOYMENTS and 
    # make an object of keys to delete
    keys_to_remove = list()
    for key in sorted_keys[MAX_DEPLOYMENTS:]:
        for obj in results_sorted:
            if obj["Key"].startswith(f"{key}/"):
                # Create a dict inside the list to match the request syntax
                # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_objects.html
                keys_to_remove.append({"Key": obj["Key"]})
    
    print("Deleting following keys:")
    print(keys_to_remove)
    if keys_to_remove:
        client.delete_objects(
            Bucket=BUCKET_NAME,
            Delete={"Objects": keys_to_remove}
        )


if __name__ == '__main__':
    main()