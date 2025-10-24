import os
from pathlib import Path

pp = os.path.join("11.py")


print(Path(pp).is_file())

print(Path().home())