from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

def load_generation_prompt():
    """
    Load the generation prompt.
    """

    system_template = "당신은 유능한 대한민국 대학수학능력고사 문제 출제자입니다. 문제를 제시하면 유사한 한국어 문제를 만들어야 합니다."

    human_template = """[Question]에 문제가 주어졌을 때 해당 문제와 유사한 개념을 묻는 오지선다 문제를 생성하고, 생성한 문제에 대해 직접 풍부한 해설을 선지별로 제공해주세요. [OUTPUT]에 설명된 조건에 맞게 문제가 생성되야 합니다. 
    [Question]
    {question}

    [OUTPUT]
    📌 [문제]
    여기에는 문제가 들어가야 합니다.

    📌 [선지]
    여기에는 5개의 선지가 ①, ②, ③, ④, ⑤로 표시되어야 합니다.

    📌 [해설]
    선지별로 ①, ②, ③, ④, ⑤로 표시하여 해설을 제공합니다.

    📌 [정답]
    ①, ②, ③, ④, ⑤ 중 정답인 번호가 하나만 표시합니다.
    """

    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(system_template),
            HumanMessagePromptTemplate.from_template(human_template)
        ]
    )

    return prompt
