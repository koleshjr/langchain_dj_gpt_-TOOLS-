from langchain.agents import Tool
from spotify import start_playing_song_by_name, start_playing_song_by_lyrics



def tool_start_playing_song_by_name():
    return Tool(name="play a song given the name", func = lambda song_name: start_playing_song_by_name(song_name),
                description=f"Given a song name, start playing a song. Action Input is a string of song_name",
                return_direct=True)

def tool_start_playing_song_by_lyrics():
    return Tool(name="play a song given its lyrics", func = lambda lyrics: start_playing_song_by_lyrics(lyrics),
                description=f"Given a song lyrics, start playing that song. Action Input is a string of lyrics",#its like guiding the agent
                return_direct = True)