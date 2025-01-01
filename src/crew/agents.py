from textwrap import dedent
from crewai import Agent
from .tools import PublishToRedisTool


class MessageFilterAgents:

    # def __init__(self):
    # 	self.gmail = GmailToolkit()

    def message_filter_agent(self):
        return Agent(
            role="Senior Message Analyst",
            goal="Filter out non-essential messages which are not related to our business",
            backstory=dedent(
                """\
				As a Senior Email Analyst, you have extensive experience in message content analysis.
				You are adept at distinguishing important emails from spam, newsletters, and other
				irrelevant content. Your expertise lies in identifying key patterns and markers that
				signify the importance of an message. Filter out only the messages which are related to fruit buisness.
                Our company deals with a wide range of products and services, including fruit, vegetables, and other related items.
			    """
            ),
            verbose=True,
            allow_delegation=False,
        )

 
    def message_response_writer(self):
        return Agent(
            role="Message Response Writer",
            goal="Draft responses to user queries related to our fruit fruit business",
            backstory=dedent(
                """\
				You are a skilled writer, adept at crafting clear, concise, and effective message responses.
				Your strength lies in your ability to communicate effectively, ensuring that each response is
				tailored to address the specific needs and context of the message. 
                """
            ),
            tools=[
                PublishToRedisTool.create_draft,
            ],
            verbose=True,
            allow_delegation=False,
        )
