
from google.adk.tools import ToolContext


def initialize_incident(
    incident_id: str,
    original_report: str,
    tool_context: ToolContext
) -> dict:
    """
    Initialize a new emergency incident in session state.

    Args:
        incident_id: Unique identifier for the incident.
        original_report: Original emergency report.

    Returns:
        Incident initialization status.
    """

    if tool_context.state.get("incident") is not None:
        return {
            "status": "error",
            "message": "An incident already exists in this session."
        }

    incident = {
        "incident_id": incident_id,
        "original_report": original_report,
        "status": "REPORTED",
        "actions_taken": []
    }

    tool_context.state["incident"] = incident

    return {
        "status": "success",
        "message": "Incident initialized successfully.",
        "incident_id": incident_id
    }


def get_incident(
    tool_context: ToolContext
) -> dict:
    """
    Retrieve the current incident information.
    """

    incident = tool_context.state.get("incident")

    if incident is None:
        return {
            "status": "error",
            "message": "No active incident found."
        }

    return {
        "status": "success",
        "incident": incident
    }


def update_incident_status(
    status: str,
    tool_context: ToolContext
) -> dict:
    """
    Update the current incident status.

    Args:
        status: New incident status.
    """

    allowed_statuses = {
        "REPORTED",
        "UNDER_ASSESSMENT",
        "COORDINATING",
        "RESOLVED"
    }

    if status not in allowed_statuses:
        return {
            "status": "error",
            "message": "Invalid incident status."
        }

    incident = tool_context.state.get("incident")

    if incident is None:
        return {
            "status": "error",
            "message": "No active incident found."
        }

    incident["status"] = status
    tool_context.state["incident"] = incident

    return {
        "status": "success",
        "updated_status": status
    }


def record_incident_action(
    agent_name: str,
    action: str,
    tool_context: ToolContext
) -> dict:
    """
    Record an action performed by an AEGIS agent.

    Args:
        agent_name: Name of the agent performing the action.
        action: Description of the action.
    """

    incident = tool_context.state.get("incident")

    if incident is None:
        return {
            "status": "error",
            "message": "No active incident found."
        }

    actions = incident.get("actions_taken", [])

    actions.append({
        "agent": agent_name,
        "action": action
    })

    incident["actions_taken"] = actions
    tool_context.state["incident"] = incident

    return {
        "status": "success",
        "message": "Incident action recorded."
    }
