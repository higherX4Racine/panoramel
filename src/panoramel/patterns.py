#  Copyright (C) 2025 by Higher Expectations for Racine County

from panoramel.el_assessment import PATTERN as EL_ASSESSMENT_PATTERN
from panoramel.ela import PATTERN as ELA_PATTERN
from panoramel.forward import PATTERN as FORWARD_PATTERN
from panoramel.intervention import PATTERN as INTERVENTION_PATTERN
from panoramel.intervention_count import PATTERN as INTERVENTION_COUNT_PATTERN
from panoramel.nwea_map import PATTERN as NWEA_MAP_PATTERN
from panoramel.pearson_aims import PATTERN as PEARSON_AIMS_PATTERN
from panoramel.source import PATTERN as SOURCE_PATTERN
from panoramel.student import PATTERN as STUDENT_PATTERN

PANORAMA_PATTERNS = {
    "el_assessment": EL_ASSESSMENT_PATTERN,
    "ela": ELA_PATTERN,
    "forward": FORWARD_PATTERN,
    "intervention": INTERVENTION_PATTERN,
    "intervention_count": INTERVENTION_COUNT_PATTERN,
    "nwea_map": NWEA_MAP_PATTERN,
    "pearson_aims": PEARSON_AIMS_PATTERN,
    "source": SOURCE_PATTERN,
    "student": STUDENT_PATTERN
}
