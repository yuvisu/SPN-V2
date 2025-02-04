from datetime import datetime
from dataclasses import dataclass


@dataclass
class DataConfig():

    sampling_rate = 500

    segmenter: str = "christov"
    
    # path
    root_dir: str = "./"

    data_dir: str = "ECG-data"

    snippet_dir: str = "snippet"

    tmp_dir: str = "tmp"

    output_dir: str = "Production"

    dataset_name: str = "ICBEB"

    snippet_name: str = "christov_norm_1000.pickle"