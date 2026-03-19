# Getting Customer Stories from the Microsoft Customer Stories API

This document describes how to programmatically search and retrieve customer success stories from Microsoft's official Customer Stories portal ([www.microsoft.com/en/customers](https://www.microsoft.com/en/customers/)), using the internal search API that powers the site's filter/search UI.

---

## Background

The Microsoft Customer Stories search page at `https://www.microsoft.com/en/customers/search` loads story cards dynamically via JavaScript. The filter-driven search UI calls an internal REST API. By reverse-engineering the JavaScript bundle (`filter-search-results` component), the API endpoint and request format can be determined.

**Key file analyzed:**
```
/golf/etc.clientlibs/onecloud/components/content/reimagine/blade/filter-search-results/v2/filter-search-results/clientlibs/sites.<HASH>.min.js
```

The `OneCloudEnvironmentConstants` class in the publisher variables JS defines the base URL:
```js
static MicrosoftAPI = Object.freeze({
    "endpoint": "https://www.microsoft.com/msstoreapiprod"
});
```

The full API endpoint is:
```
https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch
```

---

## API Reference

### Endpoint

```
POST https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch
Content-Type: application/json
```

### Request Body

All fields are optional unless noted otherwise.

| Field | Type | Description |
|:---|:---|:---|
| `locale` | string | Language/region code. Use `"en-ww"` for English worldwide. |
| `top` | integer | Number of results to return per page (page size). |
| `skip` | integer | Number of results to skip (for pagination). |
| `query` | string | Free-text search query (searches title, content, product names, etc.). |
| `products` | string | Product filter. Comma-separated filter tag values (see [Product Filter Tags](#product-filter-tags)). |
| `industries` | string | Industry filter. Comma-separated filter tag values (see [Industry Filter Tags](#industry-filter-tags)). |
| `region` | string | Region filter. Comma-separated filter tag values (see [Region Filter Tags](#region-filter-tags)). |
| `businessneed` | string | Business need filter. Comma-separated filter tag values. |
| `orderBy` | string | Sort order (e.g., `"story_publish_date desc"`). |
| `IncludeVideo` | boolean | If `true`, only return stories that include a video. |
| `IncludePartner` | boolean | If `true`, only return partner stories. |

> **Note:** Filters use filter tag values prefixed with their category (e.g., `"product:azure"`, `"industry:manufacturing"`, `"region:asia/japan"`). These values come directly from the `data-filter-tag` attributes on the checkbox elements in the search page HTML.

### Response Body

```json
{
  "cards": [ ... ],
  "totalCount": 345,
  "top": 10,
  "skip": 0,
  "hasMorePages": true
}
```

| Field | Type | Description |
|:---|:---|:---|
| `cards` | array | Array of story card objects (see [Card Object Structure](#card-object-structure)). |
| `totalCount` | integer | Total number of matching stories. |
| `top` | integer | Page size used. |
| `skip` | integer | Offset used. |
| `hasMorePages` | boolean | Whether more pages of results exist. |

### Card Object Structure

Each element of `cards` has the following shape:

```json
{
  "id": "<uuid>",
  "name": "<story-slug>",
  "_ts": 1768943694,
  "content": {
    "title": "Story Title",
    "eyebrow": "Industry: Manufacturing",
    "action": {
      "ariaLabel": "Read the story ...",
      "href": "<story-slug>",
      "text": "Read the story",
      "isOpenNewTab": true,
      "locale": "en-ww"
    },
    "image": {
      "alt": "...",
      "src": "https://cdn-dynmedia-1.microsoft.com/..."
    },
    "industries": [
      { "text": "Manufacturing" }
    ],
    "footer": {
      "relatedProducts": {
        "products": [
          { "label": "Azure Functions", "url": "https://go.microsoft.com/fwlink/..." },
          { "label": "Azure App Service", "url": "..." }
        ]
      }
    },
    "quotes": [ ... ]
  }
}
```

**Key fields:**

| Field | Description |
|:---|:---|
| `name` | The story's slug ID (e.g., `"22668-coca-cola-company-azure-ai-and-machine-learning"`). |
| `content.title` | The story's display title. |
| `content.action.href` | Same as `name`; used to construct the full story URL. |
| `content.industries` | List of industries associated with the story. |
| `content.footer.relatedProducts.products` | List of Microsoft products featured in the story. |

### Constructing the Story Page URL

The full URL for an individual story page is:

```
https://www.microsoft.com/en/customers/story/<story-slug>
```

Example:

```
https://www.microsoft.com/en/customers/story/22668-coca-cola-company-azure-ai-and-machine-learning
```

---

## Examples

### 1. Full-text search for "Azure Functions" stories

```bash
curl -s -X POST \
  -H "Content-Type: application/json" \
  "https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch" \
  -d '{
    "locale": "en-ww",
    "top": 10,
    "query": "Azure Functions"
  }'
```

### 2. Search with pagination

```bash
# Page 1 (items 1–10)
curl -s -X POST \
  -H "Content-Type: application/json" \
  "https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch" \
  -d '{"locale":"en-ww","top":10,"skip":0,"query":"Azure Functions"}'

# Page 2 (items 11–20)
curl -s -X POST \
  -H "Content-Type: application/json" \
  "https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch" \
  -d '{"locale":"en-ww","top":10,"skip":10,"query":"Azure Functions"}'
```

### 3. Filter by Azure product category

```bash
curl -s -X POST \
  -H "Content-Type: application/json" \
  "https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch" \
  -d '{
    "locale": "en-ww",
    "top": 10,
    "products": "product:azure"
  }'
```

### 4. Filter by industry

```bash
curl -s -X POST \
  -H "Content-Type: application/json" \
  "https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch" \
  -d '{
    "locale": "en-ww",
    "top": 10,
    "industries": "industry:manufacturing"
  }'
```

### 5. Filter by region (Japan)

```bash
curl -s -X POST \
  -H "Content-Type: application/json" \
  "https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch" \
  -d '{
    "locale": "en-ww",
    "top": 10,
    "region": "region:asia/japan"
  }'
```

### 6. Sort by publish date (newest first)

```bash
curl -s -X POST \
  -H "Content-Type: application/json" \
  "https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch" \
  -d '{
    "locale": "en-ww",
    "top": 10,
    "query": "serverless",
    "orderBy": "story_publish_date desc"
  }'
```

### 7. Python script: find stories that mention Azure Functions in their product list

```python
import requests

def search_customer_stories(query=None, products=None, industries=None,
                             region=None, top=10, skip=0):
    url = "https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch"
    body = {"locale": "en-ww", "top": top, "skip": skip}
    if query:
        body["query"] = query
    if products:
        body["products"] = products
    if industries:
        body["industries"] = industries
    if region:
        body["region"] = region
    resp = requests.post(url, json=body)
    resp.raise_for_status()
    return resp.json()


def get_story_url(story_slug):
    return f"https://www.microsoft.com/en/customers/story/{story_slug}"


def story_uses_azure_functions(card):
    """Returns True if Azure Functions appears in the story's product list."""
    products = (
        card.get("content", {})
            .get("footer", {})
            .get("relatedProducts", {})
            .get("products", [])
    )
    return any(p.get("label") == "Azure Functions" for p in products)


# Search and filter
results = search_customer_stories(query="Azure Functions", top=20)
print(f"Total results: {results['totalCount']}")

for card in results["cards"]:
    if story_uses_azure_functions(card):
        slug = card["name"]
        title = card["content"].get("title", "")
        url = get_story_url(slug)
        print(f"\nTitle: {title}")
        print(f"URL:   {url}")
```

### 8. Fetch and parse an individual story page

After obtaining a story slug from the API, fetch the full story text:

```python
import requests
import re

def fetch_story_text(slug):
    url = f"https://www.microsoft.com/en/customers/story/{slug}"
    resp = requests.get(url)
    resp.raise_for_status()
    html = resp.text

    # Strip scripts and styles
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<style[^>]*>.*?</style>',  '', html, flags=re.DOTALL)
    html = re.sub(r'<[^>]+>', ' ', html)
    html = re.sub(r'\s+', ' ', html)

    # Decode common HTML entities
    html = (html
        .replace('&amp;', '&')
        .replace('&lt;', '<')
        .replace('&gt;', '>')
        .replace('&quot;', '"')
        .replace('&#39;', "'")
        .replace('&#43;', '+'))

    return html

# Check whether a story page mentions Azure Functions
slug = "22668-coca-cola-company-azure-ai-and-machine-learning"
text = fetch_story_text(slug)
if "azure functions" in text.lower():
    idx = text.lower().index("azure functions")
    print(text[max(0, idx - 200): idx + 500])
```

---

## Filter Tag Reference

Filter tag values are taken directly from the `data-filter-tag` HTML attributes on the search page checkbox inputs. Pass them as-is in the corresponding request body fields.

### Product Filter Tags

Use in the `products` field. Azure-related tags:

| Filter Tag | Display Name |
|:---|:---|
| `product:azure` | Azure (all) |
| `product:azure/analytics` | Analytics |
| `product:azure/azure-ai-search` | Azure AI Search |
| `product:azure/azure-machine-learning` | Azure Machine Learning |
| `product:azure/azure-openai` | Azure OpenAI |
| `product:azure/compute` | Compute |
| `product:azure/containers` | Containers |
| `product:azure/databases` | Databases |
| `product:azure/developer-tools` | Developer Tools |
| `product:azure/devops` | DevOps |
| `product:azure/hybrid-multicloud` | Hybrid & Multicloud |
| `product:azure/iaas` | IaaS |
| `product:azure/integration` | Integration |
| `product:azure/iot` | IoT |
| `product:azure/management-governance` | Management & Governance |
| `product:azure/microsoft-fabric` | Microsoft Fabric |
| `product:azure/microsoft-foundry` | Microsoft Foundry |
| `product:azure/migration` | Migration |
| `product:azure/modern-applications` | Modern Applications |
| `product:azure/networking` | Networking |
| `product:azure/optimization` | Optimization |
| `product:azure/security` | Security |
| `product:azure/storage` | Storage |
| `product:azure/vdi` | VDI |

> **Note:** "Azure Functions" is not a standalone filter category in the UI. Use a free-text `query` search (`"Azure Functions"`) to find stories that mention it. Alternatively, filter by `product:azure/modern-applications` or `product:azure/integration` and check each story page for Azure Functions mentions.

### Industry Filter Tags

Use in the `industries` field.

| Filter Tag | Display Name |
|:---|:---|
| `industry:automotive` | Automotive |
| `industry:defense` | Defense |
| `industry:education` | Education |
| `industry:energy-resources` | Energy & Resources |
| `industry:financial-services` | Financial Services |
| `industry:government` | Government |
| `industry:healthcare` | Healthcare |
| `industry:manufacturing` | Manufacturing |
| `industry:media` | Media |
| `industry:nonprofit` | Nonprofit |
| `industry:professional-services` | Professional Services |
| `industry:retail-consumer-goods` | Retail & Consumer Goods |
| `industry:technology` | Technology |
| `industry:telecommunications` | Telecommunications |
| `industry:travel-transportation` | Travel & Transportation |
| `industry:other` | Other |

### Region Filter Tags

Use in the `region` field. Selected examples:

| Filter Tag | Display Name |
|:---|:---|
| `region:asia/japan` | Japan |
| `region:asia/india` | India |
| `region:asia/singapore` | Singapore |
| `region:asia/korea` | Korea |
| `region:asia/china` | China |
| `region:north-america/united-states` | United States |
| `region:north-america/canada` | Canada |
| `region:europe/germany` | Germany |
| `region:europe/united-kingdom` | United Kingdom |
| `region:europe/france` | France |
| `region:oceania/australia` | Australia |

For the full list, inspect the `data-filter-tag` attributes on the checkboxes at `https://www.microsoft.com/en/customers/search`.

---

## Important Notes

1. **This is an internal API**, not officially documented by Microsoft. It may change without notice.

2. **"Azure Functions" is not a first-class filter.** The product filter hierarchy only goes as deep as categories like `product:azure/modern-applications`. To reliably find Azure Functions stories:
   - Use `"query": "Azure Functions"` for broad discovery.
   - Then verify each story page by fetching it and checking whether the text or product list contains "Azure Functions".

3. **Rate limiting:** No rate limiting has been observed, but use reasonable request intervals in scripts to avoid being blocked.

4. **Locale:** Use `"en-ww"` for English worldwide results. For Japanese results, try `"ja-jp"`, though story availability in Japanese varies.

5. **Story URL construction:** The story URL is always:
   ```
   https://www.microsoft.com/en/customers/story/<story-slug>
   ```
   The slug is available as `card.name` and `card.content.action.href` in the API response.
