# Video Game Price Tracker

A price tracking system for video games built with FastAPI and SQLAlchemy.

## Project Status

### Phase 1: Backend Skeleton (Completed - Jan 24, 2026)
- FastAPI server with health check endpoint
- SQLAlchemy Product model with SQLite database
- Product CRUD endpoints (Create, Read, Delete)
- Pydantic schemas for request/response validation
- Router-based project structure

### Phase 2: Data Modeling (In Progress)
- Vendor and PriceHistory models
- Foreign key relationships
- Database schema design

### Upcoming Phases
- Phase 3: Price Fetching (Steam API integration)
- Phase 4: Price History & Updates
- Phase 5: Security & Best Practices
- Phase 6: Deployment

## Features (Planned)
- Track prices from Steam
- Store historical price data
- REST API for price queries
- Extensible vendor architecture

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite (development)
- httpx

## Setup
Coming soon...

## API Endpoints

### Products
- `POST /products` - Create a new product
- `GET /products` - Get all products
- `DELETE /products/{id}` - Delete a product

## Development Progress

Track detailed progress and design decisions in commit history.
