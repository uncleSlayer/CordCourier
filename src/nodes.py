from redis.config import redis as redis_client
from datetime import datetime, timedelta
import time


class Nodes:

    def check_email(self, state):

        print("# Checking for new emails")

        all_messages = redis_client.lrange("messages", 0, -1)

        now = datetime.now(datetime.timezone.utc)
        cutoff_time = now - timedelta(hours=24)

        recent_messages = [
            item for item in all_messages if item["timestamp"] > cutoff_time
        ]

        checked_messages = (
            state["checked_message_id"] if state["checked_message_id"] else []
        )

        new_messages = []

        for msg in recent_messages:
            if msg["id"] not in checked_messages:
                new_messages.append(
                    {
                        "id": msg["id"],
                        "message": msg["message"],
                        "author_id": msg["author_id"],
                        "channel_id": msg["channel_id"],
                        "timestamp_iso": msg["timestamp_iso"],
                    }
                )

        checked_messages.extend([msg["id"] for msg in recent_messages])

        return {
            **state,
            "messages": new_messages,
            "checked_message_id": checked_messages,
        }

    def wait_next_run(self, state):
        print("## Waiting for 180 seconds")
        time.sleep(180)
        return state

    def new_messages(self, state):
        if len(state["messages"]) == 0:
            print("## No new messages")
            return "end"
        else:
            print("## New messages found")
            return "continue"
