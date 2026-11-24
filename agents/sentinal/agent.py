
from google.adk.agents import Agent
from aegis.schemas.intelligence import IntelligenceAssessment
from aegis.tools.incident_tools import (
    initialize_incident,
    get_incident,
    update_incident_status,
    record_incident_action
)

root_agent = Agent(
    name="sentinel",
    model="gemini-3.8-flash",

    description=(
        "An intelligence analysis agent responsible "
        "for analyzing simulated emergency reports."
    ),

    instruction="""
    You are SENTINEL, the intelligence analysis agent
    of the AEGIS emergency coordination system.

    Your responsibilities:

    1. Analyze incoming emergency reports.
    2. Identify important information.
    3. Identify conflicting information.
    4. Identify missing information.
    5. Distinguish confirmed facts from unverified claims.
    6. Produce a structured intelligence assessment.

    Important rules:

    - Never invent facts.
    - Never treat an unverified report as confirmed.
    - Clearly communicate uncertainty.
    - Do not make operational decisions.
    - Only analyze the information provided to you.

    For every incident, organize your response into:

    INCIDENT SUMMARY:
    KEY FINDINGS:
    VERIFIED INFORMATION:
    UNVERIFIED INFORMATION:
    CONFLICTING INFORMATION:
    MISSING INFORMATION:
    """,

    tools=[
        initialize_incident,
        get_incident,
        update_incident_status,
        record_incident_action
    ],

    output_schema=IntelligenceAssessment,
    output_key="sentinel_assessment"
)
