FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /src

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ADD . /src
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

ENV PATH="/src/.venv/bin:$PATH"

ENTRYPOINT []

EXPOSE 8888

CMD ["uvicorn", "src.run:create_app", "--host", "0.0.0.0", "--port", "8888", "--loop", "uvloop"]
