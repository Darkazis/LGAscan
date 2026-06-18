def create_summary_verdict(criteria_results):
    met_count = 0
    not_met_count = 0
    unknown_count = 0
    manual_review_count = 0

    for result in criteria_results:
        status = result["status"]

        if status == "met":
            met_count += 1
        elif status == "not_met":
            not_met_count += 1
        elif status == "unknown":
            unknown_count += 1
        elif status == "manual_review":
            manual_review_count += 1

    if met_count >= 2:
        verdict = "Potential review evidence found"
    elif unknown_count > 0 or manual_review_count > 0:
        verdict = "Insufficient evidence — manual review required"
    else:
        verdict = "No strong review evidence found"

    return {
        "summary_verdict": verdict,
        "met_count": met_count,
        "not_met_count": not_met_count,
        "unknown_count": unknown_count,
        "manual_review_count": manual_review_count,
        "total_count": len(criteria_results),
    }