from crewai import Task
from textwrap import dedent


class MessageFilterTasks:
    def filter_messages_task(self, agent, messages):
        
        return Task(
            description=dedent(
                f"""\
				Analyze a batch of messages and filter out
				non-essential ones such as newsletters, promotional content and notifications.

			    Use your expertise in message content analysis to distinguish
				important messages from the rest, pay attention to the message body and avoid messages unrelated to fruit and vegetable business.

				MESSAGES
				-------
				{messages}

				Your final answer MUST be a the relevant user ids and message content, use bullet points.
				"""
            ),
            agent=agent,
            expected_output="relevant user ids and message content",
        )

    
    def draft_responses_task(self, agent):
        return Task(
            description=dedent(
                f"""\
				Based on the user id and messages identified, draft responses for each.

				Use the tool provided to draft each of the responses.
				When using the tool pass the following input:
				
                - to (sender to be responded)
				- subject
				- message

				You MUST create all drafts before sending your final answer.
				Your final answer MUST be a confirmation that all responses have been drafted.
				"""
            ),
            agent=agent,
            expected_output="confirmation that all responses have been drafted",
        )
