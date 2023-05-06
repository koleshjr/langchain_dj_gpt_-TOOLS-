#we are going to build a langchain react library
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI# to power our agent we'll need a foundational llm model
from langchain.memory import ConversationBufferMemory # to keep a memory of agents- what you said before
from consts import llm_model_type

load_dotenv() #load the environment vars

#initialize the llm
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(max_retries = 3, temperature=0, model_name=llm_model_type) #construct the llm model

#constructor to initialize the agent
def initialize_agent_zero_shot(tools:list, is_agent_verbose: bool = True, max_iterations: int = 3, return_thought_process: bool = False):

    memory = ConversationBufferMemory(memory_key="chat_history")
    agent = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
                              verbose=is_agent_verbose,max_iterations=max_iterations, memory=memory)
    
    return agent




