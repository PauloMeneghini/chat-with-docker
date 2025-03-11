#https://adasci.org/rag-with-milvus-vector-database-and-langchain/

#pip install langchain_community
#pip install langchain_core
import random
import time
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from milvus import initialize_milvus

vector_store = initialize_milvus()

llm = Ollama(
    model='llama3',
    temperature=0
)

print(llm)

def get_contexts(pergunta):
    results = vector_store.similarity_search_with_score(pergunta)
    print(f"RESULTADOS BD: {results}")

    # Criar um novo array com os page_content e score menor 1
    relevantDocuments = [(document.page_content, score) for document, score in results if score < 1]

    print(f"Tamanho relevantDocuments {len(relevantDocuments)}")

    return relevantDocuments

def process_question(question):

    print(f"PERGUNTA: {question}")
    contexts = get_contexts(question)
    #print(contexts)

    resposta = ""

    if len(contexts) == 0:
        resposta = "Parece que essa pergunta está fora do meu tema principal, que é amamentação. Se precisar de informações ou apoio sobre amamentação, estou aqui para ajudar no que for possível!"

    else:

        prompt = PromptTemplate(
            input_variables=["context","question"],
            template="""
            # INSTRUÇÃO
            Você é um especialista em amamentação, e deve responder perguntas sobre o processo de amamentação de forma clara e detalhada. Para cada pergunta, siga a seguinte sequência de pensamento para organizar sua resposta:
            1. Explique brevemente o conceito ou termo relacionado à pergunta.
            2. Se houver mais de uma opção ou recomendação, explique cada uma.
            3. Se possível, forneça exemplos práticos ou dicas que ajudem a esclarecer a questão.
            4. Termine com uma dica de apoio ou encorajamento para mães que amamentam.

            # CONTEXTO PARA RESPOSTAS
            {context}

            # PERGUNTA
            Pergunta: {question}
            """

        )

        rag_chain = (
            {"context": RunnablePassthrough(), "question": RunnablePassthrough(), "distance": RunnablePassthrough()} 
            | prompt
            | llm
            | StrOutputParser()
        )

        resposta = rag_chain.invoke({"context": contexts, "question": question})

        contextGreaterThan08 = False

        for context, score in contexts: 
            print(f"Score: {score}")
            if score > 0.8:
                contextGreaterThan08 = True
                break

        print(contextGreaterThan08)
            
        if contextGreaterThan08 == True:
            resposta = "\n\n**AVISO** A resposta fornecida é baseada nas informações disponíveis e pode não estar 100% precisa. Recomendo confirmar com profissionais de saúde para informações totalmente confiáveis.\n\n" + resposta

    return resposta