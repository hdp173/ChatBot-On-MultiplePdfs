from langchain.memory import ConversationTokenBufferMemory
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from dotenv import load_dotenv
load_dotenv()
llm = OpenAI(temperature=0)
conversation_with_summary = ConversationChain(
    llm=llm,
    memory=ConversationTokenBufferMemory(llm=OpenAI(), max_token_limit=60),
    verbose=True
)
conversation_with_summary.predict(input="Hi, what's up?")
conversation_with_summary.predict(
    input="Just working on writing some documentation!")
conversation_with_summary.predict(input="For LangChain! Have you heard of it?")
conversation_with_summary.predict(
    input="Haha nope, although a lot of people confuse it for that")
