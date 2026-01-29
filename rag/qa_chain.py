from collections import deque


class WebsiteQA:

    def __init__(self, llm, vector_db):
        self.llm = llm
        self.vector_db = vector_db

        
        self.memory = deque(maxlen=5)

    def ask(self, question):

        
        docs = self.vector_db.similarity_search(question, k=4)

        if not docs:
            return "The answer is not available on the provided website."

        context = "\n".join([d.page_content for d in docs])

        prompt = f"""
You are a website assistant.

Answer ONLY using the website content below.

If the answer is not present, reply exactly:
"The answer is not available on the provided website."

Website Content:
{context}

Conversation History:
{list(self.memory)}

User Question:
{question}

Answer:
"""

        response = self.llm.invoke(prompt)

        answer = response.content

       
        self.memory.append({"question": question, "answer": answer})

        return answer