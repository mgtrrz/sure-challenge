import boto3
import uuid

max_deployments = 5
bucket_name = "s3-bucket-name"

endpoint_url = "http://localstack:4566"

def init():
    client = boto3.client("s3", endpoint_url=endpoint_url)
    client.create_bucket(Bucket=bucket_name)

    for x in range(10):
        # Generate x directories/objects with a random string/hash
        client.put_object(Bucket=bucket_name, Key=f"{uuid.uuid4().hex[:6]}/index.html")


def main():
    client = boto3.client("s3", endpoint_url=endpoint_url)
    result = client.list_buckets()
    print(result)


if __name__ == '__main__':
    init()
    main()