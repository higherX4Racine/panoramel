#  Copyright (C) 2025 by Higher Expectations for Racine County

from .el_assessment import ElAssessment
from .ela import Ela
from .forward import Forward
from .intervention import Intervention
from .intervention_count import InterventionCount
from .nwea_map import NweaMap
from .pearson_aims import PearsonAims
from .school import School
from .source import Source
from .student import Student

PANORAMA_CONTEXTS = {
    "el_assessment": ElAssessment,
    "ela": Ela,
    "forward": Forward,
    "intervention": Intervention,
    "intervention_count": InterventionCount,
    "nwea_map": NweaMap,
    "pearson_aims": PearsonAims,
    "school": School,
    "source": Source,
    "student": Student
}
