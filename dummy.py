from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
async def chat(final_idea: str):
    # This is a dummy response
    dummy_titles = [
        f"TITLE {final_idea}: TITLE 1",
        f"TITLE {final_idea}: TITLE 2",
        f"TITLE {final_idea}: TITLE 3",
        f"TITLE {final_idea}: TITLE 4",
        f"TITLE {final_idea}: TITLE 5",
        f"TITLE {final_idea}: TITLE 6",
        f"TITLE {final_idea}: TITLE 7",
        f"TITLE {final_idea}: TITLE 8",
        f"TITLE {final_idea}: TITLE 9",
        f"TITLE {final_idea}: TITLE 10",
        f"TITLE {final_idea}: TITLE 11",
        f"TITLE {final_idea}: TITLE 12",
        f"TITLE {final_idea}: TITLE 13",
        f"TITLE {final_idea}: TITLE 14",
        f"TITLE {final_idea}: TITLE 15",
        f"TITLE {final_idea}: TITLE 16",
        f"TITLE {final_idea}: TITLE 17",
        f"TITLE {final_idea}: TITLE 18",
        f"TITLE {final_idea}: TITLE 19",
        f"TITLE {final_idea}: TITLE 20",
        f"TITLE {final_idea}: TITLE 21",
        f"TITLE {final_idea}: TITLE 22",
        f"TITLE {final_idea}: TITLE 23",
        f"TITLE {final_idea}: TITLE 24",
        f"TITLE {final_idea}: TITLE 25",
    ]
    
    return {
        "final_idea": final_idea,
        "titles": dummy_titles
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)