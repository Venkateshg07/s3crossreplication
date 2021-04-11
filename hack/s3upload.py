import threading
import boto3
import os
import sys
from boto3.s3.transfer import TransferConfig

buckets_name_with_key = {
    "bc71608c-8b6f-499c-bd3f-8c322408636a" : ["log1a.veerum", "log1b.veerum"],
    "87c11788-df54-4dc1-acc4-09d66fb64b66" : ["log2a.veerum", "log2b.veerum"]
}

s3 = boto3.resource('s3')

def multi_part_upload_with_s3():
    config = TransferConfig(multipart_threshold=1024 * 25, max_concurrency=10,
                            multipart_chunksize=1024 * 25, use_threads=True)
    for kms, buckets in buckets_name_with_key.items():
        for bucket in buckets:
            file_path = '%s.pdf' %(bucket)
            key_path =  '%s.pdf' %(bucket)
            s3.meta.client.upload_file(file_path, bucket, key_path,
                            ExtraArgs={ "ServerSideEncryption": "aws:kms", "SSEKMSKeyId": kms },
                             Config=config
                            )
if __name__ == '__main__': 
    multi_part_upload_with_s3()

