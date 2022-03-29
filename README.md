# PyQt ProgressBar Utils
use PyQt ProgressBar like tqdm

## Install
```bash
pip install -r requirement.txt
```

## Run example
```bash
python3 main.py
```

## Usage
```python
from progress_bar_util import ProgressBarUtil

for i in ProgressBarUtil(<list>, ui.progress_bar):
    < process >

```
replace `< list >` and `< process >`