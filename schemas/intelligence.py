from pydantic import BaseModel, Field


class IntelligenceAssessment(BaseModel):
    incident_summary: str = Field(
        description="A short summary of the reported emergency."
    )

    key_findings: list[str] = Field(
        description="The most important findings from the reports."
    )

    verified_information: list[str] = Field(
        description="Information independently confirmed by available evidence. Do not treat a witness claim as an independently verified fact."
    )

    unverified_information: list[str] = Field(
        description="Claims that have been reported but not independently confirmed."
    )

    conflicting_information: list[str] = Field(
        description="Information that differs or contradicts between reports."
    )

    missing_information: list[str] = Field(
        description="Important information that is still unknown."
    )

