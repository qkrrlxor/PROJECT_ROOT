import openai
def generate_script(topic):
    # 주제에 따라 스크립트를 생성하는 로직
    return f"Generated script for topic: {topic}"
# OpenAI API 키 설정
openai.api_key = 'your-openai-api-key'

def generate_script(topic):
    prompt = f"Create a script for a video about {topic}."

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7,
        )

        script = response.choices[0].text.strip()
        return script
    except Exception as e:
        print(f"Failed to generate script: {e}")
        return None

if __name__ == "__main__":
    topic = "Python programming"  # 예시 주제
    script = generate_script(topic)
    if script:
        print(f"Generated Script for '{topic}':\n{script}")