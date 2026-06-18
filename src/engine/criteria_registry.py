"""Criteria registry for LGAScan.

Defines the road recategorisation criteria structure.
This file does not evaluate roads; it only stores the criteria metadata.
"""

VALID_STATUSES = ["met", "not_met", "unknown", "manual_review"]

CRITERIA_REGISTRY = [
    # ------------------------------------------------------------------
    # Nationally Significant State Roads
    # ------------------------------------------------------------------
    {
        "criteria_id": "S-01",
        "criteria_name": "Comprises the National Land Transport Network",
        "target_category": "Nationally Significant State Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Route is part of the Australian Government National Land Transport Network.",
        "expected_evidence": "National Land Transport Network / freight route evidence.",
    },
    {
        "criteria_id": "S-02",
        "criteria_name": "Connects Regional City to capital city or Metropolitan Centre",
        "target_category": "Nationally Significant State Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects from a Regional City to the nearest capital city or Metropolitan Centre.",
        "expected_evidence": "Route connection evidence and centre classification data.",
    },
    {
        "criteria_id": "S-03",
        "criteria_name": "Connects Metropolitan Centres",
        "target_category": "Nationally Significant State Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects from one Metropolitan Centre to another Metropolitan Centre.",
        "expected_evidence": "Route connection evidence and metropolitan centre data.",
    },
    {
        "criteria_id": "S-04",
        "criteria_name": "Connects Metropolitan Centre to nearest International Airport",
        "target_category": "Nationally Significant State Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects from a Metropolitan Centre to the nearest International Airport.",
        "expected_evidence": "Airport location and route connection evidence.",
    },
    {
        "criteria_id": "S-05",
        "criteria_name": "Connects Metropolitan Centre or Major Intermodal to closest Major Port",
        "target_category": "Nationally Significant State Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects a Metropolitan Centre or Major Intermodal Terminal to the closest Major Port.",
        "expected_evidence": "Port, intermodal, and route connection evidence.",
    },
    {
        "criteria_id": "S-06",
        "criteria_name": "Facilitates PBS Level 2B or equivalent vehicles",
        "target_category": "Nationally Significant State Road",
        "criteria_type": "mandatory",
        "is_mandatory": True,
        "description": "Route facilitates PBS Level 2B or equivalent vehicles as a minimum.",
        "expected_evidence": "NHVR PBS Level 2B or equivalent heavy vehicle access evidence.",
    },

    # ------------------------------------------------------------------
    # State Roads
    # ------------------------------------------------------------------
    {
        "criteria_id": "S-07",
        "criteria_name": "Connects major centres to each other",
        "target_category": "State Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects Metropolitan Centres, Regional Cities, Major Towns and Major Urban Centres to each other.",
        "expected_evidence": "Centre classification and route connection evidence.",
    },
    {
        "criteria_id": "S-08",
        "criteria_name": "Connects major destinations to other centre types",
        "target_category": "State Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects Major Hospitals, Major Ports, Major Intermodals, International Airports, Commercial, Industrial or Employment Centres to other centre types.",
        "expected_evidence": "Hospital, port, intermodal, airport, employment centre and route connection evidence.",
    },
    {
        "criteria_id": "S-09",
        "criteria_name": "Facilitates PBS Level 1 or equivalent vehicles",
        "target_category": "State Road",
        "criteria_type": "mandatory",
        "is_mandatory": True,
        "description": "Route facilitates PBS Level 1 or equivalent vehicles as a minimum.",
        "expected_evidence": "NHVR PBS Level 1 or equivalent heavy vehicle access evidence.",
    },
    {
        "criteria_id": "S-10",
        "criteria_name": "Connects major centres within cities, centres and urban areas",
        "target_category": "State Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects Metropolitan Centres, Regional Cities, Major Urban Centres and Major Towns to each other.",
        "expected_evidence": "Urban centre classification and route connection evidence.",
    },
    {
        "criteria_id": "S-11",
        "criteria_name": "Connects major destinations within cities, centres and urban areas",
        "target_category": "State Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects Major Hospitals, Major Ports, Major Intermodals, International Airport, Commercial, Industrial and Employment Centres to other centre types.",
        "expected_evidence": "Destination datasets and route connection evidence.",
    },

    # ------------------------------------------------------------------
    # Regional Roads
    # ------------------------------------------------------------------
    {
        "criteria_id": "R-01",
        "criteria_name": "Connects Urban Centres and Town Centres",
        "target_category": "Regional Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects Urban Centres and Town Centres to each other.",
        "expected_evidence": "Urban centre, town centre and route connection evidence.",
    },
    {
        "criteria_id": "R-02",
        "criteria_name": "Connects major destinations to Town Centres and Urban Centres",
        "target_category": "Regional Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects Major or Regional Hospitals, Major Ports, Major Intermodals, International and Regional Airports, Commercial, Industrial and Employment Centres to Town Centres and Urban Centres.",
        "expected_evidence": "Destination, centre and route connection evidence.",
    },
    {
        "criteria_id": "R-03",
        "criteria_name": "Part of the road train network",
        "target_category": "Regional Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Road is part of the road train network.",
        "expected_evidence": "NHVR road train network map evidence.",
    },
    {
        "criteria_id": "R-04",
        "criteria_name": "Facilitates GML and CML 19m B-double routes",
        "target_category": "Regional Road",
        "criteria_type": "mandatory",
        "is_mandatory": True,
        "description": "Facilitates GML and CML 19m B-double routes over 50 tonnes or equivalent vehicles as a minimum.",
        "expected_evidence": "NHVR GML/CML 19m B-double access evidence.",
    },
    {
        "criteria_id": "R-05",
        "criteria_name": "Connects centres within cities, centres and urban areas",
        "target_category": "Regional Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects Metropolitan Centres, Major Urban Centres and Major Towns to each other.",
        "expected_evidence": "Centre classification and urban route connection evidence.",
    },
    {
        "criteria_id": "R-06",
        "criteria_name": "Connects major destinations to Major Urban Centres or Major Towns",
        "target_category": "Regional Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Connects Major and Regional Hospitals, Major Ports, Major Intermodals, International and Regional Airport, Commercial, Industrial and Employment Centres to Major Urban Centres or Major Towns.",
        "expected_evidence": "Destination, centre and route connection evidence.",
    },

    # ------------------------------------------------------------------
    # Shared criteria without unique Criteria IDs in the source table
    # ------------------------------------------------------------------
    {
        "criteria_id": "COMMON-LOAD-LIMITS",
        "criteria_name": "No load limits on assets along the route",
        "target_category": "State Road / Regional Road",
        "criteria_type": "mandatory",
        "is_mandatory": True,
        "description": "There are no load limits placed on any assets along the route.",
        "expected_evidence": "Bridge, asset restriction, load limit, or council asset evidence.",
    },
    {
        "criteria_id": "COMMON-TRAFFIC-THRESHOLD",
        "criteria_name": "Meets traffic volume and heavy vehicle thresholds",
        "target_category": "State Road / Regional Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Meets the traffic volumes and heavy vehicle percentages outlined in the vehicle threshold table.",
        "expected_evidence": "ADT and heavy vehicle percentage data.",
    },
    {
        "criteria_id": "COMMON-EMERGENCY-ROUTE",
        "criteria_name": "Emergency evacuation or alternative resilience route",
        "target_category": "Regional Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Emergency evacuation route or alternative resilience route that frequently supplements State Road traffic during natural disasters.",
        "expected_evidence": "Emergency management, flood, disaster resilience, or council route evidence.",
    },
    {
        "criteria_id": "COMMON-HV-BYPASS",
        "criteria_name": "Heavy vehicle bypass of towns",
        "target_category": "State Road",
        "criteria_type": "primary",
        "is_mandatory": False,
        "description": "Road functions as a heavy vehicle bypass of towns.",
        "expected_evidence": "Freight route, bypass, traffic movement, or planning evidence.",
    },
    {
        "criteria_id": "COMMON-NO-PARALLEL-STATE-ROAD",
        "criteria_name": "Does not closely parallel an existing State Road",
        "target_category": "State Road",
        "criteria_type": "mandatory",
        "is_mandatory": True,
        "description": "Road does not closely parallel an existing State Road unless the criteria allow it.",
        "expected_evidence": "Spatial comparison with nearby State Roads.",
    },
]