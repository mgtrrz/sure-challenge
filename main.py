import boto3

max_deployments = 5
bucket_name = "s3-bucket-name"

endpoint_url = "http://localstack:4566"


def main():
    client = boto3.client("s3", endpoint_url=endpoint_url)
    result = client.list_buckets()
    print(result)


if __name__ == '__main__':
    main()