#  Copyright (C) 2025 by Higher Expectations for Racine County

from glob import glob
from importlib.resources import files
from json import load as json_load
import os

from polars import scan_csv, DataFrame, col, lit, Expr, Binary, Int64, String, Float64, Datetime

from panoramel import (
    PANORAMA_CONTEXTS,
    PANORAMA_PATTERNS,
    PANORAMA_SCHEMAS,
    PANORAMA_TYPE_MAPS
)

from smelt_py.database.models import Context, Column
from smelt_py.database.models.base import Base as BaseModel

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

INPUT_FILES = glob(os.path.join(PANORAMA_DOWNLOAD_DIR, "*.csv"))
OUTPUT_DIR = os.path.join(DATA_DIR, "Iterations", "Panoramel")


def find_or_append(context_frame: DataFrame,
                   context: Context,
                   fields: list[str] = None) -> DataFrame:
    expr = as_filter_expressions(context, fields)
    row = context_frame.filter(*expr)
    if row.height == 0:
        row = as_row(context, context_frame)
        context_frame.vstack(row, in_place=True)
    return row


def as_filter_expressions(model_item: BaseModel,
                          fields: list[str] = None) -> list[Expr]:
    if fields is None:
        fields = model_item.field_names()[1:]
    fields = [(n, getattr(model_item, n)) for n in fields]
    return [col(n) == lit(v) for n, v in fields]


def as_row(model_item: BaseModel, template_frame: DataFrame) -> DataFrame:
    return DataFrame([model_item.as_tuple()],
                     schema=template_frame.schema,
                     orient="row")


def text_to_context(text: str, context_label: str) -> Context | None:
    captures = PANORAMA_PATTERNS[context_label].extract(text)
    if captures:
        return PANORAMA_CONTEXTS[context_label](
            **PANORAMA_TYPE_MAPS[context_label].typed_captures(captures)
        )
    return None

MEASURE_FRAMES = {
    key: DataFrame(schema={
        'measure_id': Binary,
        'column_id': Binary,
        'row': Int64,
        'value': data_type
    }) for key, data_type in [
        ("<class 'str'>", String),
        ("<class 'int'>", Int64),
        ("<class 'float'>", Float64),
        ("<class 'datetime.date'>", Datetime),
    ]
}

COLUMN_FRAME = DataFrame(schema={
    'source_id': Binary,
    'index': Int64,
    'context_type': String,
    'context_id': Binary,
    'measure_type': String
})

HEADING_KEYS = (
    {"source"}
    .symmetric_difference(PANORAMA_PATTERNS.keys())
)

CONTEXT_FRAMES = {
    k: DataFrame(schema=schema)
    for k, schema in PANORAMA_SCHEMAS.items()
}

with files("panoramel").joinpath("data", "schools.json").open() as fh:
    for pair in json_load(fh):
        school_context = PANORAMA_CONTEXTS["school"](*pair)
        CONTEXT_FRAMES["school"].vstack(
            DataFrame([school_context.as_tuple()],
                      schema=CONTEXT_FRAMES["school"].schema,
                      orient="row"),
            in_place=True
        )

for fn in INPUT_FILES:
    source_context = text_to_context(os.path.basename(fn), "source")
    find_or_append(CONTEXT_FRAMES["source"], source_context)
    school_row = find_or_append(CONTEXT_FRAMES["school"],
                                source_context,
                                ["full_name"])
    column_names = scan_csv(fn).collect_schema().names()
    for col_index, col_name in enumerate(column_names):
        for heading_key in HEADING_KEYS:
            heading_context = text_to_context(col_name, heading_key)
            if heading_context is not None:
                context_row = find_or_append(CONTEXT_FRAMES[heading_key],
                                             heading_context)
                column = Column(source_context.context_id, col_index,
                                heading_key, heading_context.context_id,
                                repr(heading_context.output_type))
                COLUMN_FRAME.vstack(as_row(column, COLUMN_FRAME), in_place=True)


def safely_print_binaries(frame, path):
    (frame
    .with_columns(
        col(Binary).bin.encode("hex")
    ).write_csv(
        path
    ))


for label, frame in CONTEXT_FRAMES.items():
    safely_print_binaries(frame,
                          os.path.join(OUTPUT_DIR, f'{label}.csv'))

safely_print_binaries(COLUMN_FRAME,
                      os.path.join(OUTPUT_DIR, 'columns.csv'))
