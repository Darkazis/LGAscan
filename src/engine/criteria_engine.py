"""Criteria evaluation engine for LGAScan."""

from engine.criteria_registry import CRITERIA_REGISTRY
from mockdata.sample_data import get_sample_criteria_results_by_road_id


def evaluate_road(selected_road, supporting_data):
    """Evaluate a selected road against the criteria registry.

    For now, this returns mock criteria results where available.
    Later, each placeholder result can be replaced with real evidence-based logic.
    """
    road_id = selected_road["road_id"]

    mock_results = get_sample_criteria_results_by_road_id(road_id)

    results_by_id = {
        result["criteria_id"]: result
        for result in mock_results
    }

    criteria_results = []

    for criterion in CRITERIA_REGISTRY:
        criteria_id = criterion["criteria_id"]

        if criteria_id in results_by_id:
            criteria_results.append(results_by_id[criteria_id])
        else:
            criteria_results.append(
                {
                    "road_id": road_id,
                    "criteria_id": criteria_id,
                    "criteria_name": criterion["criteria_name"],
                    "target_category": criterion["target_category"],
                    "is_mandatory": criterion["is_mandatory"],
                    "status": "unknown",
                    "evidence": "No mock result available for this criterion yet.",
                    "data_source": "criteria_registry",
                    "notes": "Placeholder row generated from the criteria registry.",
                }
            )

    return criteria_results