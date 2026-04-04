# FastAPI SQLite CRUD (Todos)

## Run

```zsh
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

App: http://127.0.0.1:8000
Swagger: http://127.0.0.1:8000/docs

## Environment

Copy `.env.example` to `.env` to override defaults.

## API

Base path: `/api/v1`

- `POST /photos/upload`
- `GET /photos`
- `GET /photos/{photo_id}`
- `GET /photos/{photo_id}/download`
- `POST /todos`
- `GET /todos`
- `GET /todos/{todo_id}`
- `PATCH /todos/{todo_id}`
- `DELETE /todos/{todo_id}`

### Example

```zsh
curl -X POST http://127.0.0.1:8000/api/v1/todos \
  -H 'Content-Type: application/json' \
  -d '{"title":"Buy milk","description":"2 liters"}'
```

```zsh
curl -X POST http://127.0.0.1:8000/api/v1/photos/upload \
  -F "file=@/path/to/photo.jpg"
```
