import boto3

# .env
AWS_ACCESS_KEY_ID = 'your_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'
AWS_STORAGE_BUCKET_NAME = 'bucket1'
AWS_S3_ENDPOINT_URL = 'http://s3mock:9090'
AWS_S3_REGION_NAME = 'us-east-1'

client = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                  endpoint_url=AWS_S3_ENDPOINT_URL
                  )
