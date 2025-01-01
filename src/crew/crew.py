from crewai import Crew

from .agents import MessageFilterAgents
from .tasks import MessageFilterTasks


class EmailFilterCrew:

    def __init__(self):

        agents = MessageFilterAgents()

        self.filter_agent = agents.message_filter_agent()
        self.writer_agent = agents.message_response_writer()

    def kickoff(self, state):

        print("### Filtering messages")

        tasks = MessageFilterTasks()

        crew = Crew(
            agents=[self.filter_agent, self.writer_agent],
            tasks=[
                tasks.filter_messages_task(self.filter_agent, [ { "author_id": msg["author_id"], "message": msg["message"] } for msg in state["messages"] ]),
                tasks.draft_responses_task(self.writer_agent),
            ],
            verbose=True,
        )

        result = crew.kickoff()

        return {**state, "action_required_discord_message_id": result}
