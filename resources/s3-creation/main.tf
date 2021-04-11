resource "aws_s3_bucket" "source" {
    acl             = "private"
    bucket_prefix   = var.bucket_prefix

    versioning {
        enabled = true
    }

    server_side_encryption_configuration {
        rule {
            apply_server_side_encryption_by_default {
                kms_master_key_id = aws_kms_key.srckey.arn
                sse_algorithm     = "aws:kms"
            }
        }
    }

    replication_configuration {
        role = aws_iam_role.s3replication.arn
        rules {
            prefix = ""
            status = "Enabled"

             destination {
                bucket        = aws_s3_bucket.destination.arn
                replica_kms_key_id = aws_kms_key.destkey.arn
                storage_class = "STANDARD"
            }
            source_selection_criteria {
                sse_kms_encrypted_objects {
                    enabled = "true"
                }
            }
        }
        
    }

    tags = {
        Env = var.env
    }
}