import qrcode
from pathlib import Path

url = "https://muchammadwr.my.canva.site/"

output_path = Path.cwd() / "images" / "github_qr.png"
output_path.parent.mkdir(parents=True, exist_ok=True)

qr = qrcode.make(url)
qr.save(output_path)

print(f"QR Code successfully saved at: {output_path.resolve()}")