#  Copyright (C) 2025 by Higher Expectations for Racine County

from .contexts.el_assessment import SCHEMA as EL_ASSESSMENT_SCHEMA
from .contexts.ela import SCHEMA as ELA_SCHEMA
from .contexts.forward import SCHEMA as FORWARD_SCHEMA
from .contexts.intervention import SCHEMA as INTERVENTION_SCHEMA
from .contexts.intervention_count import SCHEMA as INTERVENTION_COUNT_SCHEMA
from .contexts.nwea_map import SCHEMA as NWEA_MAP_SCHEMA
from .contexts.pearson_aims import SCHEMA as PEARSON_AIMS_SCHEMA
from .contexts.school import SCHEMA as SCHOOL_SCHEMA
from .contexts.source import SCHEMA as SOURCE_SCHEMA
from .contexts.student import SCHEMA as STUDENT_SCHEMA

PANORAMA_SCHEMAS = {
    "el_assessment": EL_ASSESSMENT_SCHEMA,
    "ela": ELA_SCHEMA,
    "forward": FORWARD_SCHEMA,
    "intervention": INTERVENTION_SCHEMA,
    "intervention_count": INTERVENTION_COUNT_SCHEMA,
    "nwea_map": NWEA_MAP_SCHEMA,
    "pearson_aims": PEARSON_AIMS_SCHEMA,
    "school": SCHOOL_SCHEMA,
    "source": SOURCE_SCHEMA,
    "student": STUDENT_SCHEMA,
}
