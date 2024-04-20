#!/bin/bash

bucket_name="s3-bucket-name"

awslocal s3api create-bucket --bucket "${bucket_name}"

awslocal s3api put-object --bucket "${bucket_name}" --key cd094fb0

awslocal s3api put-object --bucket "${bucket_name}" --key 040cc3f3

awslocal s3api put-object --bucket "${bucket_name}" --key d069a882

awslocal s3api put-object --bucket "${bucket_name}" --key f9c6a90d

awslocal s3api put-object --bucket "${bucket_name}" --key bdfb8711

awslocal s3api put-object --bucket "${bucket_name}" --key ec287e05

awslocal s3api put-object --bucket "${bucket_name}" --key c1e6b554