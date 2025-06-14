# FastAPI + Coolify Deployment Guide
<img width="741" alt="logo" src="https://github.com/user-attachments/assets/ee88457e-5886-4e88-8d17-8224442379cf" />

This repository demonstrates how to deploy a FastAPI application using Coolify with minimal setup.

## Quick Start

### Project Structure
```
fastapi-coolify/
├── main.py
└── requirements.txt
```

## Setup Instructions

### Step 1: Configure FastAPI in Coolify Dashboard

1. **Login to Coolify Dashboard**
2. Click **"+ New"** → **"Application"**
3. Select **"GitHub"**
   <img width="800" alt="Select GitHub" src="https://github.com/user-attachments/assets/0c33b781-6d1a-489e-a3ba-4f2d1a3c1242" />
4. Paste the repository link: `https://github.com/t19cs033/fastapi-coolify/`
   <img width="800" alt="Paste the repository link" src="https://github.com/user-attachments/assets/55d13e2a-44b5-4809-a6a3-eb316dcac90e" />
5. **Set Port Number** (we used port 8003, but you can set any port freely. If you change it, make sure to update the port in your source code as well)
   <img width="800" alt="Set Port Number" src="https://github.com/user-attachments/assets/05c2527e-0c70-4d17-a06e-9e8c8db61ec4" />
6. If using **Cloudflare Tunnel**, specify in Domains: `fastapi.yourdomain.com:8003`
   <img width="800" alt="Cloudflare Tunnel domain" src="https://github.com/user-attachments/assets/a80ab1d0-9f1d-4a66-9f49-b5a3b12a5402" />
8. Click **"Deploy"** button (this takes about 45 seconds)

### Step 2: Verify Deployment

Access `fastapi.yourdomain.com` and you should see:
```json
{"message":"Hello World!","status":"success"}
```

If this appears, your deployment was successful.

## Using Cloudflare Tunnel (Recommended)

If you don't want to open ports on localhost or cloud instances, use Cloudflare Tunnel.

**Benefits:**
- No need to open firewall ports
- Automatic HTTPS
- Enhanced security
- Better performance

**Setup Guide:** https://coolify.io/docs/knowledge-base/cloudflare/tunnels/overview

## Code Files

### main.py
```python
from fastapi import FastAPI
import os

app = FastAPI(title="My FastAPI App")

@app.get("/")
def read_root():
    return {"message": "Hello World!", "status": "success"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Coolify configuration
if __name__ == "__main__":
    import uvicorn
    PORT = int(os.environ.get("PORT", 8003))
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)
```

### requirements.txt
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
```

## Configuration Notes

- **Host Configuration**: Use `host="0.0.0.0"` (not `localhost`)
- **Port Flexibility**: Port can be customized, just ensure consistency between Coolify settings and source code
- **Auto-Detection**: Coolify and Nixpacks automatically detect Python environment from `requirements.txt`
- **No Additional Config**: No need for `nixpacks.toml` or `Dockerfile`

## Resources

- [Coolify Documentation](https://coolify.io/docs)
- [Cloudflare Tunnel Setup](https://coolify.io/docs/knowledge-base/cloudflare/tunnels/overview)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## Development

**Local Testing:**
```bash
pip install -r requirements.txt
python main.py
# Access: http://localhost:8003
```

**API Documentation:**
- Interactive docs: `http://yourdomain.com/docs`
- OpenAPI schema: `http://yourdomain.com/openapi.json`

---
