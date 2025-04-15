#  Copyright (C) 2025 by Higher Expectations for Racine County

from glob import glob
import os

from panoramel import Workflow

DATA_DIR = os.path.join(os.path.expanduser("~"),
                        "Documents",
                        "Data",
                        )

PANORAMA_DOWNLOAD_DIR = os.path.join(DATA_DIR,
                                     "Downloads",
                                     "Racine Unified",
                                     "Early Literacy Continuous Improvement",
                                     "2024-25",
                                     "Panorama")

workflow = Workflow()

for fn in glob(os.path.join(PANORAMA_DOWNLOAD_DIR, "*.csv")):
    workflow(fn)

workflow.save_as_spreadsheet(os.path.join(DATA_DIR, "Iterations", "Panoramel", "findings.xlsx"))
