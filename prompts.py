from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

def load_generation_prompt():
    """
    Load the generation prompt.
    """

    system_template = "당신은 유능한 대한민국 대학수학능력고사 문제 출제자입니다. 문제를 제시하면 유사한 한국어 문제를 만들어야 합니다."

    human_template = """[Qustion]에 문제가 주어졌을 때 해당 문제와 유사한 개념을 묻는 오지선다 문제를 만들고, 풍부한 해설을 선지별로 제공해주세요.
    [Question]
    {question}
    """

    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_template),
            HumanMessagePromptTemplate.from_template(human_template)
        ]
    )

    return prompt
