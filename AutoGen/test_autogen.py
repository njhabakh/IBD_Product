import os
import asyncio

from autogen_core.components.models import OpenAIChatCompletionClient, UserMessage


os.environ['OPENAI_API_KEY'] = os.getenv('Key_OpenAI')
os.environ['SERPER_API_KEY'] = os.getenv('Key_Serper')


async def run():
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o",
        # api_key=os.getenv['OPENAI_API_KEY'] # Optional if you have an OPENAI_API_KEY env variable set.
    )

    model_client_result = await model_client.create(
        messages=[
            UserMessage(content="What is the capital of France?", source="user"),
        ]
    )

    print(model_client_result)  # "Paris"

if __name__ == '__main__':
    # Create an OpenAI model client.
    run()
