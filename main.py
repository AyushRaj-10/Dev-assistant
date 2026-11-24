
import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from sentinel.agent import root_agent


APP_NAME = "aegis"
USER_ID = "operator_001"


async def main():

    # 1. Create session service
    session_service = InMemorySessionService()

    # 2. Create a session
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID
    )

    # 3. Create Runner
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    # 4. Prepare emergency report
    emergency_report = """
    An emergency report has been received.

    Location: Sector 12, North District.

    Report 1:
    A local resident reports that a building
    has collapsed following an explosion.

    Report 2:
    A nearby shopkeeper reports seeing smoke
    but does not confirm a building collapse.

    Report 3:
    An emergency caller claims that approximately
    20 people may be trapped inside.

    No official emergency team has verified
    these reports yet.
    """

    # 5. Convert report into ADK message
    message = types.Content(
        role="user",
        parts=[
            types.Part(text=emergency_report)
        ]
    )

    # 6. Execute SENTINEL
    events = runner.run(
        user_id=USER_ID,
        session_id=session.id,
        new_message=message
    )

    # 7. Read agent response
    for event in events:

        if event.is_final_response():

            print("\n========== SENTINEL REPORT ==========\n")

            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        print(part.text)

            print("\n=====================================\n")


if __name__ == "__main__":
    asyncio.run(main())
