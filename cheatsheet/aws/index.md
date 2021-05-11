
# AWS CLI

## References

| Title                       | URL                                                                             |
|-----------------------------|---------------------------------------------------------------------------------|
| Docs EKS(pt-br)             | https://docs.aws.amazon.com/pt_br/eks/latest/userguide/eks-ug.pdf               |

### Commands

#### First Steps

```
aws configure
```

#### EKS

```
eksctl create cluster \
--name my-cluster \
--region us-west-2 \
--fargate

```
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
eksctl delete cluster --name my-cluster --region us-west-2
```