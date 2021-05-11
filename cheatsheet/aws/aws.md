
# AWS CLI

## References

| Title                       | URL                                                                             |
|-----------------------------|---------------------------------------------------------------------------------|
| Docs EKS(pt-br)             | https://docs.aws.amazon.com/pt_br/eks/latest/userguide/eks-ug.pdf               |
| Terraformando o EKS         | https://www.youtube.com/playlist?list=PLsyPhquWMjqGGqK0Q43ifzkEEX7TXbuj0        |

### Commands

#### Example AWS Services

```
1. Amazon EC2 (Elastic Compute Cloud)
2. Amazon RDS (Relational Database Services)
3. Amazon S3 (Simple Storage Service)
4. Amazon Lambda
5. Amazon CloudFront
6. Amazon Glacier
7. Amazon SNS (Simple Notification Service)
8. Amazon EBS (Elastic Block Store)
9. Amazon VPC (Virtual Private Cloud)
10. Amazon Kinesis
11. Amazon Elastic Container Registry (ECR)
12. Amazon Elastic Container Service (ECS)
13. Amazon Redshift
14. Amazon CloudWatch
15. Amazon Route 53
```

#### First Steps

```
aws configure
```

#### EKS

:heavy_dollar_sign: fargate

```
eksctl create cluster \
--name my-cluster \
--region us-west-2 \
--fargate

```

:heavy_dollar_sign: managed

```
aws ec2 create-key-pair --region us-west-2 --key-name myKeyPair

eksctl create cluster \
--name my-cluster \
--region us-west-2 \
--with-oidc \
--ssh-access \
--ssh-public-key <your-key> \
--managed
```

```
# Delete cluster EKS
eksctl delete cluster --name my-cluster --region us-west-2
```