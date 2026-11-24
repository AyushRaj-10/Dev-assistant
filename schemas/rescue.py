
from typing import Literal

from pydantic import BaseModel, Field


class RescuePriority(BaseModel):

    target: str = Field(
        description="Person, group, or area requiring rescue attention. Do not invent identifiable victims."
    )

    priority: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL"
    ] = Field(
        description="Suggested rescue attention priority."
    )

    justification: str = Field(
        description="Evidence-based explanation for the suggested priority."
    )

    evidence_status: Literal[
        "VERIFIED",
        "UNVERIFIED",
        "ESTIMATED",
        "UNKNOWN"
    ] = Field(
        description="Evidence classification supporting this priority."
    )


class SafetyRisk(BaseModel):

    risk: str = Field(
        description="Potential hazard associated with the emergency."
    )

    severity: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL"
    ] = Field(
        description="Potential severity of the identified hazard."
    )

    precaution: str = Field(
        description="Recommended precaution for qualified response personnel."
    )


class RescuePlan(BaseModel):

    response_summary: str = Field(
        description="Summary of the emergency response situation."
    )

    rescue_priorities: list[RescuePriority] = Field(
        description="Suggested priorities for rescue assessment."
    )

    identified_risks: list[SafetyRisk] = Field(
        description="Potential hazards and associated safety precautions."
    )

    evacuation_considerations: list[str] = Field(
        description="Potential evacuation requirements and considerations."
    )

    immediate_recommendations: list[str] = Field(
        description="Advisory recommendations for qualified emergency responders."
    )

    missing_information: list[str] = Field(
        description="Information needed before a reliable response plan can be developed."
    )
