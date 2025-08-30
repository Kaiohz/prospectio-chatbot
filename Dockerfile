FROM python:3.12.8-slim AS builder

WORKDIR /app

# Install build dependencies
RUN pip install --upgrade pip && \
	pip install poetry

# Disable poetry virtualenv creation
RUN poetry config virtualenvs.create false

# Copy only dependency files first for better caching
COPY ./pyproject.toml ./
COPY ./poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy source code
COPY ./prospectio_chatbot ./prospectio_chatbot

# Final stage: minimal runtime image
FROM python:3.12.8-slim AS app
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /app/prospectio_chatbot ./prospectio_chatbot

EXPOSE 8000

CMD ["python", "-m", "chainlit", "run", "prospectio_chatbot/chainlit.py", "--host", "0.0.0.0"]
