import os
import pandas as pd
def load_data(filename, path, env):
    if env in [1,2]:
        file_path = os.path.join(path, filename)
    elif env == 3:
        from google.colab import drive
        drive.mount("/content/drive", force_remount=True)
        file_path = os.path.join(drive_path, file_name)
    return pd.read_csv(file_path)
    