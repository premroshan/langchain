from langchain.agents import create_agent

def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

agent = create_agent(
    model="claude-sonnet-4-5-20260929",
    tools=[get_weather],
    system_prompt="You are a helpful assistant."
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

print(response)
