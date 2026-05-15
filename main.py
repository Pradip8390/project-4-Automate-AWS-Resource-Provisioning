import subprocess

print("Creating IAM Role...")
subprocess.run(["python", "create_iam.py"])

print("Creating S3 Bucket...")
subprocess.run(["python", "create_s3.py"])

print("Launching EC2 Instance...")
subprocess.run(["python", "create_ec2.py"])

print("All Resources Created Successfully 🚀")