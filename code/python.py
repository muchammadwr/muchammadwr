import qrcode
from pathlib import Path

url = "https://github.com/muchammadwr"
output_path = Path(
    r"C:\Users\asusa\OneDrive\Dokumen\muchammadwr\images\github_qr.png"
)
output_path.parent.mkdir(parents=True, exist_ok=True)

qr = qrcode.make(url)
qr.save(output_path)

print(f"QR Code Success save at: {output_path}")