from langchain.tools import tool
from src.redis.config import redis as redis_client
import json
from pydantic import BaseModel

class DraftInput(BaseModel):
    to: str
    subject: str
    message: str


class PublishToRedisTool:
    @tool("Create Draft", args_schema=DraftInput)
    def create_draft(to: str, subject: str, message: str) -> str:
        
        """
        Useful to create an message draft.
        The input to this tool should be in the following format:
        {
            "to": "user_id",
            "subject": "subject",
            "message": "message"
        }
        """ 

        try:

            user_id = to
            subject = subject
            message = message

            message_data = {"to": user_id, "subject": subject, "message": message}

            message_to_publish = json.dumps(message_data)

            redis_client.publish("message_responses", message_to_publish)

            return f"Message published to Redis channel 'message_responses'"

        except Exception as e:

            return f"Error while publishing to Redis: {str(e)}"
