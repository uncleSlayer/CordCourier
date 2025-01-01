from src.graph import WorkFlow

app = WorkFlow().app
app.invoke({
    "checked_message_id": [],
    "messages": [],
    "action_required_discord_message_id": ""
})