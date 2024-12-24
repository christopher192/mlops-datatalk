# MLOps Maturity Model

## Create AWS EC2
1. Go to `AWS EC2` then `launch instances`.
2. Setup up based on these images.

![](images/setup-1.png)

![](images/setup-2.png)

![](images/setup-3.png)

## 
| Level | Description | Information |
| -------- | -------- | -------- |
| 0 | No MLOps | - All code in Jupyter |
| 1 | DevOps, no MLOps | - |
| 2 | Automated Training | - Training Pipeline <br> - Experiment Tracking <br> - Model Registry |
| 3 | Automated Model Deployment | - A/B Test <br> - Model Monitoring |
| 4 | Full MLOps Automated Operation | - Trigger retraining based on production metric <br> - Automatic Training <br> - Automatic Deployment |