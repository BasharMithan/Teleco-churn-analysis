import kagglehub

# Download latest version
path = kagglehub.dataset_download("blastchar/telco-customer-churn", output_dir="data/raw")

print("Path to dataset files:", path)