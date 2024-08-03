# dummy.py is only for testing the backend.
# The team is currently using freemium version of the Replicate API. Will replace later on.
# Replace the content of .env file with another Replicate API should the usage expires.

import os
import re
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import replicate

load_dotenv()

api_token = os.getenv("REPLICATE_API_TOKEN")
api = replicate.Client(api_token=api_token)

app = FastAPI()

# Add CORS middleware to allow requests from your TypeScript frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/chat")
def chat(final_idea: str):
    input = {
        "top_k": 50,
        "top_p": 0.9,
        "prompt": final_idea,
        "temperature": 0.85,
        "system_prompt": f"Create 25 titles based on the idea: {final_idea}. Answer accordingly. Don't explain too much.",
        "max_new_tokens": 512,
        "prompt_template": "<s>[INST] {system_prompt} {prompt} [/INST] "
    }

    output = replicate.run(
        "mistralai/mistral-7b-instruct-v0.2",
        input=input
    )
    
    # Join the tokens into a single string
    response_text = ''.join(output)
    
    # Process the response text
    titles = []
    for line in response_text.split('\n'):
        # Remove numbers, quotes, and backslashes
        clean_line = re.sub(r'^[0-9]+\.?\s*|["\\]', '', line.strip())
        if clean_line:
            titles.append(clean_line)
    
    return {
        "final_idea": final_idea,
        "titles": titles
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)