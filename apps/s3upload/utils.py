import boto3
import requests
from django.conf import settings


def assume_role(role_arn: str, session_name: str):
    """
    Assume an AWS IAM role and obtain temporary security credentials.

    Args:
        role_arn (str): The Amazon Resource Name (ARN) of the role to assume.
        session_name (str): A name for the assumed role session.

    Returns:
        dict: A dictionary containing temporary security credentials,
              including 'AccessKeyId', 'SecretAccessKey',
              'SessionToken', and 'Expiration'.
    """
    sts_client = boto3.client(
        'sts',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
    )

    # # Assume the role
    response = sts_client.assume_role(
        RoleArn=role_arn,
        RoleSessionName=session_name,
    )
    # Get temporary credentials
    return response['Credentials']


def get_boto3_client(service: str, **options):
    """Get boto3 client for specific service.

    Arguments:
        service (str): name of service, for example "s3"
    """

    credentials = assume_role(
        role_arn=settings.AWS_ROLE_ARN,
        session_name=settings.AWS_SESSION_NAME,
    )

    params = dict(
        region_name=settings.AWS_S3_REGION_NAME,
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials['SessionToken'],
    )

    params.update(options)
    return boto3.client(service, **params)


def create_presigned_url(
    bucket_name: str,
    object_name: str,
    expiration=3600,
    max_size=settings.ATTACHMENTS_SIZE_LIMIT,
):
    """Generate a presigned URL S3 POST request to upload a file.

    Generated url and POST data should be used to upload image/video directly
    to s3.

    Arguments:
        bucket_name (str): name of the bucket
        object_name (str): future file path
        expiration (int): time in seconds for the presigned URL to remain valid
        max_size (int): maximum size in bytes of the file to be uploaded
    """
    s3_client = get_boto3_client("s3")

    # The result contains the presigned URL and required fields
    return s3_client.generate_presigned_post(
        bucket_name,
        object_name,
        Fields={
            "success_action_status": 201,
            "acl": "public-read",
        },
        Conditions=[
            {"acl": "public-read"},
            {"success_action_status": "201"},
            ["content-length-range", 1, max_size],
        ],
        ExpiresIn=expiration,
    )


def upload_file_with_presigned_url(presigned_url: str, file_path: str):
    """Helper func to upload a local file with presigned url."""
    try:
        with open(file_path, 'rb') as file:
            files = {"file": (file_path, file)}
            response = requests.post(
                url=presigned_url["url"],
                data=presigned_url["fields"],
                files=files,
            )

        # Check if the upload was successful (HTTP status code 200-299)
        response.raise_for_status()
        print(
            f"File uploaded successfully. Status Code: {response.status_code}",
        )
    except requests.exceptions.RequestException as e:
        print(f"Error uploading file: {e}")
