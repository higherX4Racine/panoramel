#  Copyright (C) 2025 by Higher Expectations for Racine County

import glob
import os

from xlsxwriter import Workbook

from panoramel import Workflow

os.chdir(
    r"C:\Users\benta\Documents\Data\Downloads\Racine Unified\Early Literacy Continuous Improvement\2024-25\Panorama")
PANORAMA_FILES = glob.glob("*.csv")

workflow = Workflow()

columns = workflow.identify_columns(PANORAMA_FILES[0],
                                    workflow.get_column_headings(PANORAMA_FILES[0]))

with Workbook("foo.xlsx") as workbook:
    workflow.save_as_sheet(workbook, "Fratt Columns", workflow._column_framer)
