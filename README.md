# CI/CD Learning Demo

A minimal Flask app used to learn Docker + GitHub Actions hands-on.

## Files
- `app.py` — the Flask API
- `test_app.py` — pytest tests
- `requirements.txt` — Python dependencies
- `Dockerfile` — containerizes the app
- `.github/workflows/ci.yml` — GitHub Actions CI pipeline

## Run locally
```bash
pip install -r requirements.txt
python app.py
# visit http://localhost:5000
```

## Run tests
```bash
pytest test_app.py -v
```

## Run with Docker
```bash
docker build -t cicd-demo .
docker run -p 5000:5000 cicd-demo
```

## How to see CI/CD in action
1. Create a new GitHub repo
2. Push this entire folder to it
3. Go to the "Actions" tab on GitHub — you'll see the workflow run automatically
4. Try breaking a test on purpose (e.g. change an assertion) and push again — watch it fail
5. Fix it and push again — watch it pass
