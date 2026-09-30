from ai_agents.prompting.langcahin_summary_engine.llm_models import get_llm
from ai_agents.prompting.langcahin_summary_engine.utilities import to_obj
from ai_agents.prompting.langcahin_summary_engine.prompts import (
    ASSISTANT_SELECTION_PROMPT_TEMPLATE, 
)
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

assistant_instructions_chain = (
    {'user_question': RunnablePassthrough()} 
    | ASSISTANT_SELECTION_PROMPT_TEMPLATE 
    | get_llm() | StrOutputParser() | to_obj
)