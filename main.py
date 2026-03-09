from fastapi import FastAPI

from teacher_routes import router as teacher_routes
app = FastAPI(
    title="C Clarke Institute"
)

app.include_router(teacher_routes)