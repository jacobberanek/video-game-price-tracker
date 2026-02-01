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

### Phase 3: Price Fetching (✅Completed - Feb 1, 2026)
- Integrated Steam API for price fetching
- Implemented modular price fetcher architecture to support multiple game stores in future
- Added error handling and logging
- Created price update endpoints
- Built vendor management system
- Tested end-to-end flow
  
### Phase 4: Price History & Updates (In Progress)
- Build price history query endpoints with date filtering
- Add batch update endpoint for multiple products
- Implement background tasks for automated updates
- Add price comparison across vendors

### Upcoming Phases
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

### Health
- `GET /health` - Health check endpoint

### Products
- `POST /products` - Create a new product
- `GET /products` - Get all products
- `DELETE /products/{product_id}` - Delete a product

### Vendors
- `POST /vendors` - Create a new vendor
- `GET /vendors` - Get all vendors
- `DELETE /vendors/{vendor_id}` - Delete a vendor

### Prices
- `POST /prices/update/{product_id}` - Fetch and store current price for a product (only steam games for now)
- `GET /prices/{product_id}` - Get price history for one product


## Development Progress

Track detailed progress and design decisions in commit history.
