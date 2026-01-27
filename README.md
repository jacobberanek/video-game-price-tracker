# Video Game Price Tracker

A price tracking system for video games built with FastAPI and SQLAlchemy.

## Project Status

### Phase 1: Backend Skeleton (✅Completed - Jan 24, 2026)
- FastAPI server with health check endpoint
- SQLAlchemy Product model with SQLite database
- Product CRUD endpoints (Create, Read, Delete)
- Pydantic schemas for request/response validation
- Router-based project structure

### Phase 2: Data Modeling (✅Completed - Jan 27, 2026)
- Designed normalized database schema (products, vendors, price_history)
- Created Vendor and PriceHistory models with foreign key relationships
- Implemented SQLAlchemy ORM relationships for bidirectional querying
- Added Pydantic schemas for all models with proper validation
- Tested relationships work correctly (product.prices, price.vendor, etc.)

### Phase 3: Price Fetching (In Progress)
- Implement price fetching from Steam API
- Create vendor-agnostic fetcher architecture (Strategy Pattern)
- Add error handling and rate limiting
- Store fetched prices in price_history table

### Upcoming Phases
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
