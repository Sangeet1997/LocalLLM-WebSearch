from fetchURL import fetch_urls
from getContent import extract_text_from_url
import ollama
import asyncio



def handleQuery(query, num = 5):
    urls = asyncio.run(fetch_urls(query))
    if num > len(urls):
        num = len(urls)

    content = ""
    for i in range(num):
        url = urls[i]
        content += url + "\n"
        content += extract_text_from_url(url) + "\n"

    model_prompt = f"""
            Your task is to summarize the content provided into one conclusive article according to the user query.
            You should also cite the sources with numbers. EXAMPLE: "THE SKY IS BLUE[4]."

            content: {content}
            user query: {query}

            ***RETURN ONLY THE SUMMARIZED CONTENT***
        """

    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": model_prompt}])
    print(response["message"]["content"].strip())
    return

def main():
    while True:
        query = input("Enter your query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        
        num = int(input("Enter number of sources you want to check: "))
        handleQuery(query, num)

if __name__ == "__main__":
    main()