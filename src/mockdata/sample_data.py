"""
Temporary sample data for early dashboard development.

Purpose
-------
This file gives each developer stable mock objects to build against before the
real processed datasets and module connections are finished.

Important
---------
- This is NOT final project data.
- Do not treat these values as official analysis outputs.
- The object shapes here should imitate the real processed files we expect later.
- Keep this file small enough to stay readable, but detailed enough to unblock UI,
  map, data loading, criteria, and results development.

Expected processed files later
------------------------------
data/processed/processed_roads.geojson
data/processed/processed_supporting_evidence.csv
data/processed/processed_criteria_results.csv
data/processed/processed_summary_results.csv
"""

# ---------------------------------------------------------------------------
# Shared status values
# ---------------------------------------------------------------------------

VALID_STATUSES = ["met", "not_met", "unknown", "manual_review"]

VALID_CONFIDENCE_LEVELS = ["low", "medium", "high"]


# ---------------------------------------------------------------------------
# SAMPLE_ROADS
# ---------------------------------------------------------------------------
# Imitates future: data/processed/processed_roads.geojson
#
# Raw data this is loosely based on:
# - raw/nsw_road_network_categorisation/nsw_road_network_categorisation.csv
#
# Real processed road records should eventually include geometry so the map can
# display the selected road. For now, geometry is kept as None so the app can be
# developed without requiring real spatial processing immediately.

SAMPLE_ROADS = [
    {
        "road_id": "0000027,0042,C2/3",
        "road_name": "GOLDEN HIGHWAY",
        "road_number": "27",
        "current_category": "State",
        "admin_class": "S",
        "lga": "Upper Hunter",
        "start_point": "Sample start point",
        "end_point": "Sample end point",
        "length_km": 0.137,
        "geometry": None,
    },
    {
        "road_id": "0006003,1390,C4/1",
        "road_name": "M1 - SYDNEY-NEWCASTLE FREEWAY",
        "road_number": "6003",
        "current_category": "State",
        "admin_class": "S",
        "lga": "Central Coast",
        "start_point": "Sample start point",
        "end_point": "Sample end point",
        "length_km": 7.496,
        "geometry": None,
    },
    {
        "road_id": "0000061,0174,A2/1",
        "road_name": "ORANGE-CONDOBOLIN",
        "road_number": "61",
        "current_category": "State",
        "admin_class": "S",
        "lga": "Orange",
        "start_point": "Sample start point",
        "end_point": "Sample end point",
        "length_km": 1.740,
        "geometry": None,
    },
    {
        "road_id": "0000011,0168,C1",
        "road_name": "OXLEY",
        "road_number": "11",
        "current_category": "State",
        "admin_class": "S",
        "lga": "Port Macquarie-Hastings",
        "start_point": "Sample start point",
        "end_point": "Sample end point",
        "length_km": 0.243,
        "geometry": None,
    },
]

SAMPLE_SELECTED_ROAD = SAMPLE_ROADS[0]


# ---------------------------------------------------------------------------
# SAMPLE_SUPPORTING_EVIDENCE
# ---------------------------------------------------------------------------
# Imitates future: data/processed/processed_supporting_evidence.csv
#
# Purpose:
# A consolidated road-level evidence table. This is the kind of data the
# dashboard should use after heavy preprocessing has already been completed.
#
# Each row is one road or road segment with precomputed evidence fields.
# This lets the Streamlit dashboard stay lightweight.

SAMPLE_SUPPORTING_EVIDENCE = [
    {
        "road_id": "0000027,0042,C2/3",
        "nearest_centre_name": "Newcastle",
        "nearest_centre_type": "Major Urban Centre",
        "nearest_centre_population": 348539,
        "distance_to_centre_km": 42.0,
        "adt": 39273,
        "heavy_vehicle_percent": 8.2,
        "freight_access_type": "B-double / heavy vehicle evidence placeholder",
        "has_load_limit": False,
        "load_limit_notes": "No load-limit evidence in sample data.",
        "near_hospital": "unknown",
        "near_airport": True,
        "nearest_airport_name": "PORT MACQUARIE AIRPORT",
        "near_port": "unknown",
        "near_intermodal": "unknown",
        "emergency_route_flag": "unknown",
        "evidence_notes": "Sample evidence combines simplified road, traffic, centre, freight, and airport-style fields.",
    },
    {
        "road_id": "0006003,1390,C4/1",
        "nearest_centre_name": "Central Coast",
        "nearest_centre_type": "Major Urban Centre",
        "nearest_centre_population": 325255,
        "distance_to_centre_km": 5.0,
        "adt": None,
        "heavy_vehicle_percent": None,
        "freight_access_type": "Motorway / freight evidence placeholder",
        "has_load_limit": "unknown",
        "load_limit_notes": "Load-limit evidence not loaded in sample data.",
        "near_hospital": "unknown",
        "near_airport": "unknown",
        "nearest_airport_name": None,
        "near_port": "unknown",
        "near_intermodal": "unknown",
        "emergency_route_flag": "unknown",
        "evidence_notes": "Traffic value intentionally left missing to test unknown handling.",
    },
    {
        "road_id": "0000061,0174,A2/1",
        "nearest_centre_name": "Orange",
        "nearest_centre_type": "Regional City / Regional Centre placeholder",
        "nearest_centre_population": 40127,
        "distance_to_centre_km": 3.5,
        "adt": 8200,
        "heavy_vehicle_percent": 6.8,
        "freight_access_type": "Heavy vehicle access placeholder",
        "has_load_limit": False,
        "load_limit_notes": "No load-limit evidence in sample data.",
        "near_hospital": "unknown",
        "near_airport": "unknown",
        "nearest_airport_name": None,
        "near_port": False,
        "near_intermodal": "unknown",
        "emergency_route_flag": "unknown",
        "evidence_notes": "Regional sample road used to test regional threshold-style outputs.",
    },
]


# This dictionary form is convenient for criteria_engine.py.
# It lets code quickly find evidence by road_id.
SAMPLE_SUPPORTING_DATA = {
    "supporting_evidence": SAMPLE_SUPPORTING_EVIDENCE,
    "traffic": [
        {
            "station_key": "57723",
            "station_id": "92277",
            "road_id": "0000027,0042,C2/3",
            "road_name": "Golden Highway",
            "lga": "Upper Hunter",
            "year": 2018,
            "period": "WEEKDAYS",
            "adt": 39273,
            "heavy_vehicle_percent": 8.2,
            "latitude": -32.129383,
            "longitude": 150.269196,
            "data_source": "NSW traffic counts sample fields",
        },
        {
            "station_key": "58612",
            "station_id": "97340",
            "road_id": "0000011,0168,C1",
            "road_name": "Oxley Avenue",
            "lga": "Carrathool",
            "year": 2022,
            "period": "ALL DAYS",
            "adt": None,
            "heavy_vehicle_percent": None,
            "latitude": -33.480766,
            "longitude": 145.534805,
            "data_source": "NSW traffic station reference sample fields",
        },
    ],
    "centres": [
        {
            "centre_id": "UCL102004",
            "centre_name": "Newcastle",
            "centre_type": "Major Urban Centre",
            "population_2021": 348539,
            "section_of_state": "Major Urban",
            "area_sqkm": 296.9898,
            "geometry": None,
            "data_source": "ABS UCL 2021 sample fields",
        },
        {
            "centre_id": "UCL112017",
            "centre_name": "Port Macquarie",
            "centre_type": "Regional City / Regional Centre placeholder",
            "population_2021": 47793,
            "section_of_state": "Other Urban",
            "area_sqkm": 43.8921,
            "geometry": None,
            "data_source": "ABS UCL 2021 sample fields",
        },
        {
            "centre_id": "UCL112016",
            "centre_name": "Orange",
            "centre_type": "Regional City / Regional Centre placeholder",
            "population_2021": 40127,
            "section_of_state": "Other Urban",
            "area_sqkm": 56.8283,
            "geometry": None,
            "data_source": "ABS UCL 2021 sample fields",
        },
    ],
    "airports": [
        {
            "airport_id": "AIRPORT_0003",
            "airport_name": "PORT MACQUARIE AIRPORT",
            "airport_type": "Regional Airport placeholder",
            "longitude": 152.86750477687465,
            "latitude": -31.430606596605426,
            "operational_status": 1,
            "urbanity": "S",
            "data_source": "NSW Airport FOI Transport Facilities sample fields",
        },
        {
            "airport_id": "AIRPORT_0093",
            "airport_name": "GOULBURN AIRPORT",
            "airport_type": "Regional Airport placeholder",
            "longitude": 149.7328991915149,
            "latitude": -34.80715969591481,
            "operational_status": 1,
            "urbanity": "S",
            "data_source": "NSW Airport FOI Transport Facilities sample fields",
        },
    ],
    "freight": [
        {
            "road_id": "0000027,0042,C2/3",
            "network_type": "B-double placeholder",
            "allowed": True,
            "notes": "Sample freight access value only; replace with NHVR-derived evidence later.",
        },
        {
            "road_id": "0000061,0174,A2/1",
            "network_type": "B-double placeholder",
            "allowed": True,
            "notes": "Sample freight access value only; replace with NHVR-derived evidence later.",
        },
    ],
    "load_limits": [
        {
            "asset_id": "LOAD_ASSET_001",
            "road_id": "0000027,0042,C2/3",
            "asset_type": "Bridge placeholder",
            "has_load_limit": False,
            "load_limit_tonnes": None,
            "notes": "Sample only. Real load-limit evidence still needs reliable source data.",
        },
        {
            "asset_id": "LOAD_ASSET_002",
            "road_id": "0006003,1390,C4/1",
            "asset_type": "Bridge placeholder",
            "has_load_limit": "unknown",
            "load_limit_tonnes": None,
            "notes": "Unknown value included to test manual/unknown handling.",
        },
    ],
}


# ---------------------------------------------------------------------------
# SAMPLE_CRITERIA_RESULTS
# ---------------------------------------------------------------------------
# Imitates future: data/processed/processed_criteria_results.csv
#
# Purpose:
# A criteria-by-road output table. Each row represents one criterion checked for
# one selected road.

SAMPLE_CRITERIA_RESULTS = [
    {
        "road_id": "0000027,0042,C2/3",
        "criteria_id": "R-01",
        "criteria_name": "Connects Urban Centres and Town Centres",
        "target_category": "Regional",
        "is_mandatory": False,
        "status": "manual_review",
        "evidence": "Sample road has nearby centre evidence, but connection/path logic is not implemented yet.",
        "data_source": "sample_data",
        "notes": "Use this to test manual review display.",
    },
    {
        "road_id": "0000027,0042,C2/3",
        "criteria_id": "R-04",
        "criteria_name": "Facilitates GML & CML 19m B-double routes or equivalent vehicles",
        "target_category": "Regional",
        "is_mandatory": True,
        "status": "met",
        "evidence": "Sample freight evidence marks this road as B-double accessible.",
        "data_source": "sample_data",
        "notes": "Replace with NHVR-derived evidence later.",
    },
    {
        "road_id": "0000027,0042,C2/3",
        "criteria_id": "R-Self Assess-02",
        "criteria_name": "Meets traffic volumes and heavy vehicle percentage thresholds",
        "target_category": "Regional",
        "is_mandatory": False,
        "status": "met",
        "evidence": "Sample ADT is 39,273 and heavy vehicle percentage is 8.2%.",
        "data_source": "sample_data",
        "notes": "Threshold logic still needs to be implemented properly.",
    },
    {
        "road_id": "0000027,0042,C2/3",
        "criteria_id": "R-Self Assess-04",
        "criteria_name": "There are no load limits placed on any assets along the route",
        "target_category": "Regional",
        "is_mandatory": True,
        "status": "unknown",
        "evidence": "No reliable route-level load-limit dataset is connected in sample data.",
        "data_source": "sample_data",
        "notes": "Use this to test unknown/missing-evidence display.",
    },
    {
        "road_id": "0000027,0042,C2/3",
        "criteria_id": "S-08",
        "criteria_name": "Connects to major hospitals, ports, intermodals, airports, or employment centres",
        "target_category": "State",
        "is_mandatory": False,
        "status": "manual_review",
        "evidence": "Sample airport proximity exists, but route connection and airport significance logic are not implemented.",
        "data_source": "sample_data",
        "notes": "Use this to test destination evidence display.",
    },
]


# ---------------------------------------------------------------------------
# SAMPLE_SUMMARY_RESULTS
# ---------------------------------------------------------------------------
# Imitates future: data/processed/processed_summary_results.csv
#
# Purpose:
# One high-level dashboard row per road. This is what can drive the main road
# screening table/cards.

SAMPLE_SUMMARY_RESULTS = [
    {
        "road_id": "0000027,0042,C2/3",
        "road_name": "GOLDEN HIGHWAY",
        "current_category": "State",
        "potential_target_category": "Regional or State review",
        "summary_verdict": "Potential review evidence found",
        "confidence": "low",
        "met_count": 2,
        "not_met_count": 0,
        "unknown_count": 1,
        "manual_review_count": 2,
        "reason": "Sample evidence shows freight and traffic indicators, but connection and load-limit evidence still need real processing/manual review.",
    },
    {
        "road_id": "0006003,1390,C4/1",
        "road_name": "M1 - SYDNEY-NEWCASTLE FREEWAY",
        "current_category": "State",
        "potential_target_category": "State",
        "summary_verdict": "Current category appears supported",
        "confidence": "low",
        "met_count": 1,
        "not_met_count": 0,
        "unknown_count": 3,
        "manual_review_count": 1,
        "reason": "Sample record is a State motorway-style road, but most criteria evidence is placeholder only.",
    },
    {
        "road_id": "0000061,0174,A2/1",
        "road_name": "ORANGE-CONDOBOLIN",
        "current_category": "State",
        "potential_target_category": "Regional or State review",
        "summary_verdict": "Insufficient evidence",
        "confidence": "low",
        "met_count": 1,
        "not_met_count": 0,
        "unknown_count": 3,
        "manual_review_count": 1,
        "reason": "Sample regional evidence exists, but full criteria assessment has not been connected.",
    },
]

SAMPLE_SUMMARY_VERDICT = SAMPLE_SUMMARY_RESULTS[0]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
# These are optional convenience helpers. They keep early UI/engine testing simple
# without forcing every developer to write the same lookup code.

def get_sample_road_by_id(road_id):
    """Return a sample road dictionary by road_id, or None if not found."""
    for road in SAMPLE_ROADS:
        if road["road_id"] == road_id:
            return road
    return None


def get_sample_supporting_evidence_by_road_id(road_id):
    """Return consolidated sample supporting evidence for a road_id."""
    for row in SAMPLE_SUPPORTING_EVIDENCE:
        if row["road_id"] == road_id:
            return row
    return None


def get_sample_criteria_results_by_road_id(road_id):
    """Return sample criteria result rows for a road_id."""
    return [row for row in SAMPLE_CRITERIA_RESULTS if row["road_id"] == road_id]


def get_sample_summary_result_by_road_id(road_id):
    """Return sample summary result for a road_id, or None if not found."""
    for row in SAMPLE_SUMMARY_RESULTS:
        if row["road_id"] == road_id:
            return row
    return None
