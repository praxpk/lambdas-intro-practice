import boto3


class S3Client:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self.client = boto3.client("s3")
            self.resource = boto3.resource("s3")
            self._initialized = True


def list_files_in_bucket(bucket):
    client = S3Client()
    bucket_obj = client.resource.Bucket(bucket)
    files = []
    for file in bucket_obj.objects.all():
        files.append(file.key)
    return files


def get_buckets():
    client = S3Client()
    buckets = []
    resp = client.client.list_buckets()
    for bucket in resp["Buckets"]:
        buckets.append(bucket["Name"])
    return buckets
