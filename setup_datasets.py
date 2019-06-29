import os
import shutil

import global_vars as Global
"""
Unpack data on temporary storage location 
"""
CACHE_PATH = os.path.join(os.environ.get("SLURM_TMPDIR"),'data')

if __name__ == "__main__":
    assert os.path.exists(os.path.expanduser(CACHE_PATH))

    for dataset in Global.all_dataset_classes:
        if 'name' in dataset.__dict__:
            print("working on ", dataset.name)
            try:
                set = dataset(root_path=os.path.join(CACHE_PATH, dataset.name), download=False, extract=True)
            except RuntimeError:
                pass
            print("complete ", dataset.name)