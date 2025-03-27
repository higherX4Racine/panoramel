#  Copyright (C) 2025 by Higher Expectations for Racine County

from datetime import datetime

import pytest

from panoramel import SourceContext, PANORAMA_PATTERNS, PANORAMA_TYPE_MAPS

SOURCE_NAMES = [
    "FrattElementary_students_ELA_YTD_20250211085843.csv",
    "Gifford_students_ELA_YTD_20250211090050.csv",
    "GilmoreFineArtsSchool_students_ELA_YTD_20250211090108.csv",
    "GoodlandMontessori_students_ELA_YTD_20250211090130.csv",
    "Jerstad-AgerholmSchool_students_ELA_YTD_20250211090146.csv",
    "JulianThomasElementary_students_ELA_YTD_20250211090206.csv",
    "KnappElementary_students_ELA_YTD_20250211090232.csv",
    "MitchellSchool_students_ELA_YTD_20250211090251.csv",
    "OlympiaBrownElementary_students_ELA_YTD_20250211090313.csv",
    "RedAppleSchool_students_ELA_YTD_20250211090336.csv",
    "RooseveltElementary_students_ELA_YTD_20250211090353.csv",
    "SchulteSchool_students_ELA_YTD_20250211090422.csv",
    "SCJohnsonElementary_students_ELA_YTD_20250211090406.csv",
    "StarbuckInternationalSchool_students_ELA_YTD_20250211090449.csv",
    "WadewitzElementary_students_ELA_YTD_20250211090509.csv",
]

SCHOOL_NAMES = [
    "FrattElementary",
    "Gifford",
    "GilmoreFineArtsSchool",
    "GoodlandMontessori",
    "Jerstad-AgerholmSchool",
    "JulianThomasElementary",
    "KnappElementary",
    "MitchellSchool",
    "OlympiaBrownElementary",
    "RedAppleSchool",
    "RooseveltElementary",
    "SchulteSchool",
    "SCJohnsonElementary",
    "StarbuckInternationalSchool",
    "WadewitzElementary",
]

TIME_STAMPS = [
    (8, 58, 43),
    (9, 0, 50),
    (9, 1, 8),
    (9, 1, 30),
    (9, 1, 46),
    (9, 2, 6),
    (9, 2, 32),
    (9, 2, 51),
    (9, 3, 13),
    (9, 3, 36),
    (9, 3, 53),
    (9, 4, 22),
    (9, 4, 6),
    (9, 4, 49),
    (9, 5, 9),
]


@pytest.mark.parametrize("text,school,timestamp",
                         zip(SOURCE_NAMES, SCHOOL_NAMES, TIME_STAMPS))
def test_source_context(text, school, timestamp):
    captures = PANORAMA_PATTERNS["source"].extract(text)
    assert captures[0].value == school
    timestring = ''.join(f'{x:02}' for x in timestamp)
    assert captures[1].value == "20250211" + timestring
    context = SourceContext(
        **PANORAMA_TYPE_MAPS["source"].typed_captures(captures),
        context_id=b"1"
    )
    assert context.full_name == school
    assert context.date_stamp == datetime(2025, 2, 11, *timestamp)
    assert context.output_name is None
    assert context.output_type is None
