from ai_agents import initialize_agent_zero_shot #zero since you don't give it any examples
from ai_tools import tool_start_playing_song_by_lyrics,tool_start_playing_song_by_name

#initialize tools

tools = [
    tool_start_playing_song_by_name(),
    tool_start_playing_song_by_lyrics()
]

agent = initialize_agent_zero_shot(tools = tools)
print("\nIt's your boy DJ NGENIgpt can I take your requests?")

while True:
    request = input("n\nRequest: ")
    result = agent({"input": request})
    answer = result["output"]

    print(answer)