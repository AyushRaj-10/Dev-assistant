
from google.adk.agents import ParallelAgent, SequentialAgent

from aegis.agents.sentinal.agent import root_agent as sentinel_agent
from aegis.agents.relay.agent import root_agent as relay_agent
from aegis.agents.supplynet.agent import root_agent as supplynet_agent
from aegis.agents.rescue.agent import root_agent as rescue_agent


# Run RELAY, SUPPLYNET and RESCUE concurrently.
response_analysis = ParallelAgent(
    name="response_analysis",
    description=(
        "Coordinates communication, resource and rescue "
        "planning agents concurrently."
    ),
    sub_agents=[
        relay_agent,
        supplynet_agent,
        rescue_agent
    ]
)


# First analyze the incident, then perform parallel planning.
root_agent = SequentialAgent(
    name="aegis_coordinator",
    description=(
        "The central coordinator of AEGIS responsible "
        "for orchestrating emergency intelligence and "
        "response planning agents."
    ),
    sub_agents=[
        sentinel_agent,
        response_analysis
    ]
)
