from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="Agentic AI Code Assistant")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global agent instance
agent = None

@app.on_event("startup")
async def startup_event():
    global agent
    agent = LlamaCodeAgent()

@app.post("/api/edit-line")
async def edit_line(request: dict):
    """Edit a single line of code"""
    try:
        file_path = request.get('file_path')
        line_number = request.get('line_number')
        new_content = request.get('new_content')
        
        # Process the edit
        # Implementation depends on your specific setup
        
        return {"success": True, "message": "Line edited successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket for real-time interaction"""
    await websocket.accept()
    
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            
            # Process message with agent
            response = agent.process_message(message)
            
            await websocket.send_text(json.dumps(response))
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()
