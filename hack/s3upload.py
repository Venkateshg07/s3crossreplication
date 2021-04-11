import threading
import boto3
import os
import sys
from boto3.s3.transfer import TransferConfig
BUCKET_NAME = "veerumassign20210410162734799500000002"

s3 = boto3.resource('s3')

def multi_part_upload_with_s3():
    config = TransferConfig(multipart_threshold=1024 * 25, max_concurrency=10,
                            multipart_chunksize=1024 * 25, use_threads=True)
    file_path = 'largefile.pdf'
    key_path = 'largefile.pdf'

    s3.meta.client.upload_file(file_path, BUCKET_NAME, key_path,
                            ExtraArgs={ "ServerSideEncryption": "aws:kms", "SSEKMSKeyId":"9956e54b-7420-4914-8cb4-ab18ad79f213" },
                             Config=config
                            )
if __name__ == '__main__': 
    multi_part_upload_with_s3()
