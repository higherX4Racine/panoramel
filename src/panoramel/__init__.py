#  Copyright (C) 2025 by Higher Expectations for Racine County
r"""Classes that describe heading data in parsed tables"""

from .el_assessment import ElAssessment as ElAssessmentContext
from .ela import Ela as ElaContext
from .forward import Forward as ForwardContext
from .intervention import Intervention as InterventionContext
from .intervention_count import InterventionCount as InterventionCountContext
from .nwea_map import NweaMap as NweaMapContext
from .pearson_aims import PearsonAims as PearsonAimsContext
from .school import School as SchoolContext
from .source import Source as SourceContext
from .student import Student as StudentContext


PANORAMA_CONTEXTS = {
    "el_assessment": ElAssessmentContext,
    "ela": ElaContext,
    "forward": ForwardContext,
    "intervention": InterventionContext,
    "intervention_count": InterventionCountContext,
    "nwea_map": NweaMapContext,
    "pearson_aims": PearsonAimsContext,
    "source": SourceContext,
    "student": StudentContext
}