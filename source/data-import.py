import kagglehub
from pathlib import Path

data_dir = Path("data/raw")
data_dir.mkdir(parents=True, exist_ok=True)

# Download the latest version into data/raw and rename its CSV file.
path = kagglehub.dataset_download(
	"blastchar/telco-customer-churn", output_dir=str(data_dir)
)
download_path = Path(path)
csv_file = download_path if download_path.is_file() else next(download_path.rglob("*.csv"))
renamed_path = data_dir / "teleco-churn-data.csv"
csv_file.rename(renamed_path)

print("Path to dataset file:", renamed_path)