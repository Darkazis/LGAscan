"""Criteria registry for LGAScan.

This file defines the criteria structure only.
It does not evaluate whether a road meets each criterion.
"""

VALID_STATUSES = ["met", "not_met", "unknown", "manual_review"]

CRITERIA_REGISTRY = [
    {
        "criteria_id": "R-01",
        "criteria_name": "Connects Urban Centres and Town Centres",
        "target_category": "Regional",
        "is_mandatory": False,
        "description": "Checks whether the road connects relevant urban or town centres.",
        "expected_evidence": "Centre proximity and route connection evidence.",
    },
    {
        "criteria_id": "R-04",
        "criteria_name": "Facilitates GML & CML 19m B-double routes or equivalent vehicles",
        "target_category": "Regional",
        "is_mandatory": True,
        "description": "Checks whether the road supports approved heavy vehicle access.",
        "expected_evidence": "NHVR or freight access evidence.",
    },
    {
        "criteria_id": "R-Self Assess-02",
        "criteria_name": "Meets traffic volumes and heavy vehicle percentage thresholds",
        "target_category": "Regional",
        "is_mandatory": False,
        "description": "Checks traffic volume and heavy vehicle percentage indicators.",
        "expected_evidence": "ADT and heavy vehicle percentage.",
    },
    {
        "criteria_id": "R-Self Assess-04",
        "criteria_name": "There are no load limits placed on any assets along the route",
        "target_category": "Regional",
        "is_mandatory": True,
        "description": "Checks whether bridges or other assets along the route have load limits.",
        "expected_evidence": "Load-limit or bridge restriction evidence.",
    },
    {
        "criteria_id": "S-08",
        "criteria_name": "Connects to major hospitals, ports, intermodals, airports, or employment centres",
        "target_category": "State",
        "is_mandatory": False,
        "description": "Checks whether the road connects to major strategic destinations.",
        "expected_evidence": "Hospital, port, airport, intermodal, or employment centre evidence.",
    },
]