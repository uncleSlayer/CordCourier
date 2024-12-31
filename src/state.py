from typing import TypedDict

class DiscordMessageState(TypedDict):
	checked_message_id: list[str]
	messages: list[dict]
	action_required_discord_message_id: str