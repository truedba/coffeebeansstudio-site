#!/usr/bin/env python3
"""prep_key.py SRC OUT — вырезать рисунок Nano Banana с пурпурного #FF00FF, сохранив РОЗОВОЕ (цветы бонсая).
Пурпурность m = min(R,B) − G: фон ≈ 255, розовые лепестки < 40. Альфа = 1 − (m−40)/80, кайма обесцвечивается.
Тот же признак, что у tools/ui_nabor.py в репозитории игры (вердикт там: ПОТЕНЦИАЛ к выносу в sprite-kit «лист на хромакее»).
Коды: 0 сделано · 2 нет аргумента/файла."""
import sys
import numpy as np
from PIL import Image
A = [x for x in sys.argv[1:] if x != "--no-crop"]
if len(A) != 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help") else 2)
a = np.asarray(Image.open(A[0]).convert("RGB")).astype(np.float32)
R, G, B = a[..., 0], a[..., 1], a[..., 2]
m = np.minimum(R, B) - G
alpha = np.clip(1 - (m - 40) / 80, 0, 1)
# снять пурпурный отсвет на кайме: подтянуть R и B к G пропорционально «фоновости»
k = 1 - alpha
a[..., 0] = R - k * np.maximum(R - G, 0) * 0.85
a[..., 2] = B - k * np.maximum(B - G, 0) * 0.85
out = np.dstack([np.clip(a, 0, 255), alpha * 255]).astype(np.uint8)
im = Image.fromarray(out); im = im if "--no-crop" in sys.argv else im.crop(im.getbbox()); im.save(A[1])
print(f"{A[1]}: {im.size}, фон убран {float((alpha < .05).mean())*100:.1f} %")
