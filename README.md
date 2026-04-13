# cafeteria360
Agente de inteligencia artificial enfocado en el turismo en el Eje Cafetero.

## Desarrollo local

Backend:

```powershell
cd backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Frontend:

```powershell
cd frontend
npm install
npm run dev -- --host 127.0.0.1 --port 5173
```

El frontend usa proxy a `/api`, por lo que no necesitas fijar `VITE_API_URL` para desarrollo si el backend corre en `127.0.0.1:8000`.

## Despliegue con Docker

El flujo de producción usa:

- `backend/` con FastAPI y Uvicorn
- `frontend/` compilado y servido por Nginx
- proxy desde Nginx hacia `backend:8000` para `/api`

Comando de despliegue:

```powershell
docker compose -f docker-compose.prod.yml up --build -d
```

La aplicación quedará disponible en el puerto `80` del servidor.

## Despliegue en Render

Este repositorio incluye un Blueprint en `render.yaml` con:

- un web service para el backend (`cafeteria360-api`)
- un static site para el frontend (`cafeteria360-web`)

Pasos:

1. Sube el repositorio a GitHub.
2. En Render, crea un nuevo Blueprint y selecciona el repositorio.
3. Cuando Render lo pida, agrega `OPENAI_API_KEY` para el servicio `cafeteria360-api`.
4. Confirma el despliegue.

Notas:

- El frontend recibirá su `VITE_API_URL` desde la URL pública del backend.
- El backend acepta `CORS_ORIGINS` tanto como JSON (`["https://..."]`) como texto simple separado por comas.
- Si usas el plan `free`, el backend puede entrar en reposo por inactividad.
