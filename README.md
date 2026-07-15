# Docker Compose Lab (Day 11)

This project demonstrates how to run a multi-container application using Docker Compose.

## Services
- **app**: Python web server
- **db**: PostgreSQL database

## Commands
docker compose up -d  
docker compose down  

## Purpose
Part of my DevOps learning path: understanding multi-container orchestration.

## Environment Variables (.env)

This project uses a `.env` file to store configuration and secrets.

Example:

POSTGRES_USER=adele
POSTGRES_PASSWORD=supersecret
POSTGRES_DB=testdb
POSTGRES_PORT=5432
APP_PORT=8000

The `.env` file is ignored using `.gitignore` and is not pushed to GitHub.
