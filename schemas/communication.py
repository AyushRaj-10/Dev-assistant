
from pydantic import BaseModel, Field
from typing import Literal


class CommunicationMessage(BaseModel):
    recipient: str = Field(
        description="The intended recipient or response team."
    )

    priority: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"] = Field(
        description="The urgency of this communication."
    )

    message: str = Field(
        description="The message prepared for the recipient."
    )


class CommunicationPlan(BaseModel):
    communication_summary: str = Field(
        description="A short summary of the communication requirements."
    )

    target_groups: list[str] = Field(
        description="Groups that need to receive relevant incident information."
    )

    priority: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"] = Field(
        description="Overall communication priority."
    )

    messages: list[CommunicationMessage] = Field(
        description="Prepared messages for different recipient groups."
    )

    information_gaps: list[str] = Field(
        description="Information needed before communication can be finalized."
    )
