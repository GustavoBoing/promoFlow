# PromoFlow

Automated affiliate promotion distribution platform powered by scraping, AI and real-time deal processing.

---

## 📌 Overview

PromoFlow is a backend-focused automation platform designed to:

- Collect promotions from marketplaces
- Process and validate deals
- Rank offers using business rules and scoring
- Generate marketing copy using AI
- Automatically distribute promotions to Telegram channels
- Store historical pricing and analytics data

The project was designed as a scalable affiliate automation ecosystem using modern backend architecture and automation pipelines.

---

## 🎯 Main Goals

- Automate affiliate promotion discovery
- Eliminate manual product posting
- Create intelligent promotion ranking
- Build a scalable distribution pipeline
- Apply real-world backend engineering concepts

---

## 🏗️ Core Architecture

```text
Marketplaces
(Amazon / Shopee / Mercado Livre)
        ↓
Data Capture
(requests / BeautifulSoup / Selenium)
        ↓
Processing Layer
(Rules Engine / Score System / AI)
        ↓
Database
(PostgreSQL)
        ↓
API Layer
(FastAPI)
        ↓
Distribution
(Telegram Channels)
```

---

## ⚙️ Tech Stack

### Backend
- Python
- FastAPI

### Web Scraping
- requests
- BeautifulSoup
- Selenium

### Database
- PostgreSQL

### Automation
- APScheduler
- Cron Jobs

### AI
- OpenAI API

### Distribution
- Telegram Bot API

### Infrastructure
- Docker
- GitHub

---

## 🚀 Features

### Promotion Capture
- Marketplace scraping
- Product extraction
- Price collection
- Metadata and image extraction

### Rules Engine
- Promotion validation
- Duplicate detection
- Category filtering
- Price comparison

### Intelligent Scoring
- Discount analysis
- Product rating validation
- Priority ranking
- Promotion quality score

### AI Copy Generation
- CTA generation
- Promotional messages
- Optimized descriptions

### Automated Distribution
- Telegram channel posting
- Scheduled publications
- Multi-category support

### Historical Tracking
- Price history
- Promotion tracking
- Analytics preparation

---

## 📂 Project Structure

```text
promoflow/
│
├── api/
├── database/
├── scraper/
├── rules/
├── scheduler/
├── telegram/
├── ai/
├── analytics/
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧠 Processing Flow

```text
Capture Promotions
        ↓
Normalize Data
        ↓
Store in Database
        ↓
Apply Business Rules
        ↓
Generate Score
        ↓
Generate AI Copy
        ↓
Publish to Telegram
```

---

## 🗄️ Database Modeling

### Products

Stores fixed product information.

```text
id
name
category
marketplace
product_url
image
brand
rating
```

### Promotions

Stores dynamic and historical promotion data.

```text
id
product_id
old_price
current_price
discount
coupon
score
priority
published
created_at
```

---

## 🧩 API Responsibilities

FastAPI acts as the central orchestration layer of the system.

### Responsibilities
- Manage scrapers
- Handle promotion rules
- Integrate AI services
- Manage Telegram publishing
- Centralize database access
- Provide analytics endpoints
- Support future admin dashboard

### Example Endpoints

```http
GET /promotions
POST /publish
GET /status
POST /scraper/shopee
GET /analytics
```

---

## ⏰ Scheduler Responsibilities

Automate recurring system tasks.

### Examples
- Execute scrapers every X minutes
- Recalculate promotion scores
- Publish approved promotions
- Remove expired deals

---

## 📢 Distribution Strategy

### Current
- Telegram Channels

### Future
- Instagram
- TikTok
- Discord
- Website
- Twitter/X

---

## 🛣️ MVP Scope

The first version of PromoFlow focuses on:

- Capturing promotions
- Saving products into the database
- Applying validation rules
- Generating promotion scores
- Publishing automatically to Telegram

---

## 🔮 Future Roadmap

- Dashboard Admin
- Analytics System
- Multi-channel Distribution
- Recommendation Engine
- Smart Scheduling
- AI-driven ranking
- Worker architecture
- SEO website integration

---

## 📚 Learning Goals

This project was also designed to improve skills in:

- Backend Engineering
- APIs
- Automation
- Web Scraping
- Software Architecture
- Database Modeling
- AI Integration
- Distributed Systems
- Product Engineering

---

## 🧪 Development Philosophy

PromoFlow is being developed incrementally:

1. Build a working MVP
2. Validate the automation flow
3. Improve scoring and intelligence
4. Scale distribution
5. Optimize monetization

---

## 📌 Project Status

🚧 In Development

---

## 👨‍💻 Author

Developed by Gustavo Boing.
