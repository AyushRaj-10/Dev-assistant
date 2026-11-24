
from typing import Any


def initialize_incident(
    state: Any,
    incident_id: str,
    original_report: str
) -> dict:

    incident = {
        "incident_id": incident_id,
        "original_report": original_report,
        "status": "REPORTED",
        "sentinel_assessment": None,
        "actions_taken": [],
    }

    state["incident"] = incident

    return incident


def get_incident(state: Any) -> dict | None:
    return state.get("incident")


def update_incident_status(
    state: Any,
    status: str
) -> dict:

    allowed_statuses = {
        "REPORTED",
        "UNDER_ASSESSMENT",
        "COORDINATING",
        "RESOLVED",
    }

    if status not in allowed_statuses:
        raise ValueError(f"Invalid incident status: {status}")

    incident = state.get("incident")

    if incident is None:
        raise ValueError("No incident has been initialized.")

    incident["status"] = status

    return incident


def store_sentinel_assessment(
    state: Any,
    assessment: dict
) -> dict:

    incident = state.get("incident")

    if incident is None:
        raise ValueError("No incident has been initialized.")

    incident["sentinel_assessment"] = assessment

    return incident


def add_incident_action(
    state: Any,
    action: dict
) -> dict:

    incident = state.get("incident")

    if incident is None:
        raise ValueError("No incident has been initialized.")

    incident["actions_taken"].append(action)

    return incident
