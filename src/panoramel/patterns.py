#  Copyright (C) 2025 by Higher Expectations for Racine County

from .contexts.el_assessment import PATTERN as EL_ASSESSMENT_PATTERN
from .contexts.ela import PATTERN as ELA_PATTERN
from .contexts.forward import PATTERN as FORWARD_PATTERN
from .contexts.intervention import PATTERN as INTERVENTION_PATTERN
from .contexts.intervention_count import PATTERN as INTERVENTION_COUNT_PATTERN
from .contexts.nwea_map import PATTERN as NWEA_MAP_PATTERN
from .contexts.pearson_aims import PATTERN as PEARSON_AIMS_PATTERN
from .contexts.source import PATTERN as SOURCE_PATTERN
from .contexts.student import PATTERN as STUDENT_PATTERN

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
