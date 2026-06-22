def create_summary_verdict(criteria_results):
    met_count = 0
    not_met_count = 0
    unknown_count = 0
    manual_review_count = 0
    mandatory_not_met_count = 0

    for result in criteria_results:
        status = result["status"]

        if status == "met":
            met_count += 1
        elif status == "not_met":
            not_met_count += 1
            if result.get("is_mandatory"):
                mandatory_not_met_count += 1
        elif status == "unknown":
            unknown_count += 1
        elif status == "manual_review":
            manual_review_count += 1

    attention_count = unknown_count + manual_review_count

    if not criteria_results:
        verdict = "No criteria selected"
        explanation = "Select a criteria set to begin the assessment."
    elif attention_count:
        verdict = "Further evidence required"
        explanation = (
            f"{attention_count} criteria cannot yet be decided because evidence "
            "is unavailable or requires review."
        )
    elif mandatory_not_met_count:
        verdict = "Mandatory criteria not satisfied"
        explanation = (
            f"{mandatory_not_met_count} mandatory criteria are not met. "
            "A final classification should not be recommended."
        )
    elif not_met_count:
        verdict = "Mixed assessment result"
        explanation = (
            f"{met_count} criteria are met and {not_met_count} are not met. "
            "Review the detailed results before making a decision."
        )
    else:
        verdict = "Criteria supported by available evidence"
        explanation = (
            "All selected criteria with available evidence are marked as met."
        )

    return {
        "summary_verdict": verdict,
        "explanation": explanation,
        "met_count": met_count,
        "not_met_count": not_met_count,
        "unknown_count": unknown_count,
        "manual_review_count": manual_review_count,
        "mandatory_not_met_count": mandatory_not_met_count,
        "total_count": len(criteria_results),
    }
