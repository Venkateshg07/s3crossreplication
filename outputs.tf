output "varname" {
  value = var.s3_bucket_names
}
output "length" {
  value = sum([for _, names in var.s3_bucket_names : length(names)])
}

output "test" {
  value = flatten([for _, names in var.s3_bucket_names : names ])
}

output "test1" {
  value = aws_s3_bucket.replica1[*].arn
}

output "test2" {
  value = [for arn in aws_s3_bucket.replica2[*].arn : "${arn}/*" ]
}