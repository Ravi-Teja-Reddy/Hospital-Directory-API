
from fastapi import FastAPI
from app.database import Base, engine
from app.routes import router
# Initialize FastAPI app
app = FastAPI(title="Hospital Directory API")

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include the API routes
app.include_router(router)
