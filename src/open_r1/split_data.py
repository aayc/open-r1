#!/usr/bin/env python3

import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

def split_dataset(input_file: Path, train_ratio: float = 0.8, val_ratio: float = 0.1, test_ratio: float = 0.1):
    # 1. Load the JSON data
    data = json.loads(input_file.read_text())
    
    # 2. Shuffle the data (so splits are random)
    random.shuffle(data)
    
    # 3. Compute split indices
    n = len(data)
    train_end = int(train_ratio * n)
    val_end = train_end + int(val_ratio * n)
    # test goes until the end
    
    # 4. Split the data
    train_data = data[:train_end]
    val_data = data[train_end:val_end]
    test_data = data[val_end:]
    
    # 5. Save splits to separate JSON files
    output_dir = input_file.parent / 'splits'
    output_dir.mkdir(exist_ok=True)
    
    with (output_dir / 'train.json').open('w') as f_train:
        json.dump(train_data, f_train, indent=2)
    
    with (output_dir / 'validation.json').open('w') as f_val:
        json.dump(val_data, f_val, indent=2)
    
    with (output_dir / 'test.json').open('w') as f_test:
        json.dump(test_data, f_test, indent=2)
    
    print(f"Data split complete.\n"
          f"Train size: {len(train_data)}, "
          f"Validation size: {len(val_data)}, "
          f"Test size: {len(test_data)}")

if __name__ == "__main__":
    # Example usage
    split_dataset(Path(BASE_DIR / "data/math_level3to5_data_processed_with_qwen_prompt.json"), train_ratio=0.8, val_ratio=0.1, test_ratio=0.1)