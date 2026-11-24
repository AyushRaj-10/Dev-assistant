
from typing import Literal

from pydantic import BaseModel, Field


class ResourceRequirement(BaseModel):

    resource_type: str = Field(
        description="Name of the required resource, such as ambulance, rescue team, firefighter or medical personnel."
    )

    purpose: str = Field(
        description="Specific purpose this resource would serve during the emergency response."
    )

    quantity_estimate: int | None = Field(
        default=None,
        ge=0,
        description="Estimated quantity required. Use None when available information is insufficient to calculate a quantity."
    )

    urgency: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL"
    ] = Field(
        description="Priority level indicating how urgently this resource may be needed."
    )

    evidence_status: Literal[
        "VERIFIED",
        "UNVERIFIED",
        "ESTIMATED",
        "UNKNOWN"
    ] = Field(
        description="Evidence classification supporting this resource recommendation."
    )

    justification: str = Field(
        description="Reason for recommending this resource based on the available incident information."
    )


class ResourcePlan(BaseModel):

    resource_summary: str = Field(
        description="Overall summary of the potential resource requirements for the incident."
    )

    requirements: list[ResourceRequirement] = Field(
        description="List of recommended resources with their estimated quantities, urgency and supporting evidence."
    )

    resource_constraints: list[str] = Field(
        description="Known limitations affecting resource requirements, availability or deployment."
    )

    missing_information: list[str] = Field(
        description="Additional information required to produce more accurate resource estimates."
    )

    operational_warnings: list[str] = Field(
        description="Safety risks, logistical concerns and operational limitations that response teams should consider."
    )
