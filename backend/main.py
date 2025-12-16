from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from database import engine
from models import Base
from routes import router

load_dotenv()
Base.metadata.create_all(bind=engine)

app = FastAPI(title="backend_api_for_p,_a_web_application_built_using_react_as_the_frontend_and_fastapi_+_sqlalchemy_as_the_backend_stack._the_goal_of_this_project_is_to_design_and_implement_a_scalable,_secure,_and_maintainable_api_to_serve_the_frontend_application. API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to backend_api_for_p,_a_web_application_built_using_react_as_the_frontend_and_fastapi_+_sqlalchemy_as_the_backend_stack._the_goal_of_this_project_is_to_design_and_implement_a_scalable,_secure,_and_maintainable_api_to_serve_the_frontend_application. API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "backend_api_for_p,_a_web_application_built_using_react_as_the_frontend_and_fastapi_+_sqlalchemy_as_the_backend_stack._the_goal_of_this_project_is_to_design_and_implement_a_scalable,_secure,_and_maintainable_api_to_serve_the_frontend_application."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)