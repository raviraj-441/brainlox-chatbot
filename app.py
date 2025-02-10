from flask import Flask, request, jsonify
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

# Custom prompt template
system_prompt = """You are an expert assistant for Brainlox technical courses. 
Always follow these rules:
1. Provide clear, structured answers with bullet points when listing courses
2. Include course descriptions and durations when available
3. Start responses directly with the answer, never use "According to the context"
4. If unsure, say "I don't have information about that course."

Current conversation:
{context}

Question: {question}
Helpful Answer:"""

custom_prompt = PromptTemplate(
    template=system_prompt,
    input_variables=['context', 'question']
)

qa_chain = RetrievalQA.from_chain_type(
    llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": custom_prompt}
)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get('query')
    
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    result = qa_chain.invoke({"query": query})
    return jsonify({
        "answer": result["result"],
        "sources": [doc.metadata for doc in result["source_documents"]]
    })

if __name__ == '__main__':
    app.run(debug=True)