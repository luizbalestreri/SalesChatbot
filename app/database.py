from flask_sqlalchemy import SQLAlchemy
from langchain_community.chat_message_histories import ChatMessageHistory
db = SQLAlchemy()
chat_history = ChatMessageHistory()
