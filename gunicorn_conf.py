import multiprocessing

# Bind to all interfaces, port 8000
bind = "0.0.0.0:8000"

# Automatically detect number of workers based on CPU count
workers = multiprocessing.cpu_count() * 2 + 1

# Use threads to handle multiple requests per worker
threads = 4

# Worker class: gthread is great for Flask if you use lightweight IO
worker_class = "gthread"

# Restart workers after handling N requests (to prevent memory leaks)
max_requests = 1000
max_requests_jitter = 50

# Logging
# accesslog = "logs/gunicorn_access.log"
# errorlog = "logs/gunicorn_error.log"
accesslog = "-"
errorlog = "-"
# loglevel = "info"



# Daemonize the Gunicorn process (not recommended with systemd or Docker)
# daemon = True  # ← uncomment only if not using systemd/docker

# Timeout (seconds): if a request takes longer, the worker is killed
timeout = 120
graceful_timeout = 30
keepalive = 5

# Preload the app: reduce memory usage with copy-on-write (if compatible)
preload_app = True

# PID file (optional, for process monitoring)
# pidfile = "gunicorn.pid"

# Set environment variables if needed
raw_env = [
    "FLASK_ENV=production",
    "APP_ENV=production"
]

# Custom headers (e.g., behind reverse proxy)
secure_scheme_headers = {
    "X-FORWARDED-PROTO": "https",
    "X-FORWARDED-SSL": "on"
}