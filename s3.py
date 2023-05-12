import boto3  # pip install boto3
import settings

session = boto3.Session(
    profile_name=settings.PROFILE,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.REGION_NAME,
)
s3 = session.resource("s3")
# Let's use Amazon S3
# s3 = boto3.resource("s3")

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)



# def connect_s3_service(bucket_name):
#     session = boto3.Session(
#         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#         region_name=settings.REGION_NAME,
#     )
#     s3 = session.resource("s3")
#     return s3.Bucket(bucket_name)

# connect_s3_service