#  Copyright (C) 2025 by Higher Expectations for Racine County

from .contexts.el_assessment import TYPE_MAP as EL_ASSESSMENT_TYPE_MAP
from .contexts.ela import TYPE_MAP as ELA_TYPE_MAP
from .contexts.forward import TYPE_MAP as FORWARD_TYPE_MAP
from .contexts.intervention import TYPE_MAP as INTERVENTION_TYPE_MAP
from .contexts.intervention_count import TYPE_MAP as INTERVENTION_COUNT_TYPE_MAP
from .contexts.nwea_map import TYPE_MAP as NWEA_MAP_TYPE_MAP
from .contexts.pearson_aims import TYPE_MAP as PEARSON_AIMS_TYPE_MAP
from .contexts.school import TYPE_MAP as SCHOOL_TYPE_MAP
from .contexts.source import TYPE_MAP as SOURCE_TYPE_MAP
from .contexts.student import TYPE_MAP as STUDENT_TYPE_MAP

PANORAMA_TYPE_MAPS = {
    "el_assessment": EL_ASSESSMENT_TYPE_MAP,
    "ela": ELA_TYPE_MAP,
    "forward": FORWARD_TYPE_MAP,
    "intervention": INTERVENTION_TYPE_MAP,
    "intervention_count": INTERVENTION_COUNT_TYPE_MAP,
    "nwea_map": NWEA_MAP_TYPE_MAP,
    "pearson_aims": PEARSON_AIMS_TYPE_MAP,
    "school": SCHOOL_TYPE_MAP,
    "source": SOURCE_TYPE_MAP,
    "student": STUDENT_TYPE_MAP,
}
