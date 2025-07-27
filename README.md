# 🚀 How to Run the Flask App (detailsapp)

This guide explains how to run the Flask-based app located in the `detailsapp` project directory.

---

## 📦 Project Structure Overview

```
.
├── Dockerfile                # Optional: for containerized deployment
├── details.py                # Entrypoint script (dev mode)
├── gunicorn_conf.py          # Gunicorn configuration (production)
├── Pipfile / Pipfile.lock    # Pipenv environment management
├── README.md                 # You're here
├── src/details/app.py        # Main Flask app instance
└── automation/               # Template automation scripts
```

---

## 🐍 1. Run in Development Mode (with Pipenv)

### Prerequisites:

- Python 3.11 installed
- `pipenv` installed (`pip install pipenv`)

```bash
cd ~/Projects/detailsapp
pipenv install       # installs packages from Pipfile
pipenv shell         # activates virtual environment
python details.py    # launches Flask dev server
```

Flask will run on:

- http\://127.0.0.1:8000
- http\://:8000

---

## 🦄 2. Run with Gunicorn (Production Server)

Make sure you're inside the pipenv shell:

```bash
pipenv shell
```

Then run:

```bash
gunicorn -c gunicorn_conf.py src.details.app:app
```

This uses:

- `gunicorn_conf.py` for production tuning
- `src.details.app:app` to load the Flask instance

---

## 🐳 3. Run in Docker (Optional)

Ensure you have Docker installed. Then build and run:

```bash
docker build -t detailsapp .
docker run -p 8000:8000 detailsapp
```

Make sure your Dockerfile:

- Copies project files
- Installs dependencies
- Uses `gunicorn` as CMD

Example CMD:

```Dockerfile
CMD ["gunicorn", "-c", "gunicorn_conf.py", "src.details.app:app"]
```

---

## 🧪 4. Automation Scripts

The `automation/` folder contains Python scripts that help:

- Download Bootstrap templates
- Configure Nginx proxying
- Automate HTML and Docker setup

You can run them like:

```bash
pipenv run python automation/download_template.py
```

---

✅ Ready to go! Use whichever method suits your environment best — dev, Docker, or production.

