import json

import pytest
from EdgeGPT.EdgeGPT import Chatbot
from EdgeGPT.EdgeGPT import ConversationStyle

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_ask():
    bot = await Chatbot.create()  # Passing cookies is "optional", as explained above
    response = await bot.ask(
        prompt="What time is it?",
        conversation_style=ConversationStyle.balanced,
        simplify_response=True,
    )
    await bot.close()
    print(json.dumps(response, indent=2))
    assert response != ""
