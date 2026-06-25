from s3 import get_buckets, list_files_in_bucket

if __name__ == "__main__":
    buckets = get_buckets()
    for bucket in buckets:
        print(list_files_in_bucket(bucket))
