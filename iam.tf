resource "aws_iam_policy" "ses_send_policy" {
  name = "LambdaSESSendEmail"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "ses:SendEmail",
          "ses:SendRawEmail"
        ],
        Effect   = "Allow",
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_policy_attachment" "attach_ses_send" {
  name       = "attach_ses_send"
  roles      = [aws_iam_role.lambda_exec_role.name]
  policy_arn = aws_iam_policy.ses_send_policy.arn
}
