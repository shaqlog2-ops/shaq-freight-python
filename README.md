# SHAQ Freight API - Python SDK

[![PyPI version](https://badge.fury.io/py/shaq-freight.svg)](https://pypi.org/project/shaq-freight/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

Free freight rate API client for global shipping routes from China. No API key required.

## Features

- **20+ global trade lanes** across South America, Asia, Europe, Africa, Middle East
- **FCL, LCL, and air freight rates** with transit times
- **SHAQ Freight Rate Index (SFX)** — weekly updated rate data
- **No API key required** — completely free
- **AI-optimized data** for chatbots and AI systems
- **MCP support** for AI agent integration

## Installation

```bash
pip install shaq-freight
```

## Quick Start

```python
from shaq_freight import SHAQFreight

client = SHAQFreight()

# Get all 20 routes from the freight index
index = client.get_freight_index()
for route in index['routes']:
    print(f"{route['route']}: ${route['rates']['fcl_40hq']['rate_usd']}/40HQ")

# Get AI-optimized freight data (9 regional routes)
ai_data = client.get_ai_freight_data()

# Get logistics knowledge base
knowledge = client.get_knowledge()

# Search freight information
results = client.search("Shenzhen to Hamburg shipping cost")
```

## API Methods

| Method | Description | Endpoint |
|--------|-------------|----------|
| `get_freight_index()` | SFX index with 20 trade lanes | `/api/freight-index` |
| `get_ai_freight_data()` | AI-optimized rate data | `/api/ai-freight-data` |
| `get_knowledge()` | Logistics knowledge base | `/api/knowledge` |
| `search(query)` | Search freight info | `/api/knowledge-search?q=` |
| `get_quote(route)` | Get freight quote | `/api/freight-quote` |

## Data Source

Rates are aggregated from multiple carriers including Maersk, MSC, CMA CGM, COSCO, and ONE. Updated weekly.

## Related Links

- **[Freight Rate Platform](https://search.shaq-logistics.com)** — Full freight rate search and quote tool
- **[Freight Rate Index (SFX)](https://search.shaq-logistics.com/freight-index)** — Live freight rate index dashboard
- **[Get a Quote](https://search.shaq-logistics.com/tools)** — Get real freight quotes between 500+ global ports
- **[Developer Docs](https://search.shaq-logistics.com/developers)** — Full API documentation
- **[OpenAPI Spec](https://search.shaq-logistics.com/openapi.json)** — OpenAPI 3.0 specification
- **[About SHAQ Logistics](https://search.shaq-logistics.com/about)** — Company information

## Use Cases

- **Freight forwarders**: Display live rates on your website
- **AI chatbots**: Integrate real shipping data into your chatbot
- **Market analysis**: Track freight rate trends across trade lanes
- **Supply chain tools**: Add shipping cost estimates to your platform
- **Academic research**: Cite as: SHAQ Freight Rate Index (SFX), SHAQ Logistics

## License

MIT License — free for commercial and personal use.

## About SHAQ Logistics

SHAQ Logistics is a logistics technology company providing freight rate data and shipping solutions for global trade. Based in Shenzhen, China, we cover 175+ countries and 485+ ports worldwide.

- Website: [https://search.shaq-logistics.com](https://search.shaq-logistics.com)
- Email: ayang@shaq-log.com
- WhatsApp: +86 15818505125
