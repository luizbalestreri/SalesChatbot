
from langchain.schema import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from app.agents import agent_executor
from .database import chat_history

def processar_mensagem(mensagem):
    # chat = ChatOpenAI(api_key=Config.OPENAI_API_KEY, model='gpt-4o-mini')

    conversational_agent_executor = RunnableWithMessageHistory(
        agent_executor,
        lambda session_id: chat_history,
        input_messages_key="messages",
        output_messages_key="output",
    )

    resposta = conversational_agent_executor.invoke(
        {"messages": [HumanMessage(mensagem)]},
        {"configurable": {"session_id": "unused"}}
    )
    print(resposta)
    return resposta['output']