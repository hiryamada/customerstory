import azure.functions as func
import logging
import requests

app = func.FunctionApp()

CUSTOMER_STORIES_API_URL = "https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch"
STORY_BASE_URL = "https://www.microsoft.com/en/customers/story"


def search_customer_stories(query, top=10, skip=0):
    """Search the Microsoft Customer Stories API."""
    body = {
        "locale": "en-ww",
        "top": top,
        "skip": skip,
        "query": query,
    }
    resp = requests.post(CUSTOMER_STORIES_API_URL, json=body, timeout=10)
    resp.raise_for_status()
    return resp.json()


def get_story_url(slug):
    """Construct the full URL for a customer story."""
    return f"{STORY_BASE_URL}/{slug}"


def format_stories(product, data):
    """Format customer stories data into a Markdown response."""
    cards = data.get("cards", [])
    total_count = data.get("totalCount", 0)

    lines = []
    lines.append(f"# {product} Customer Stories\n")
    lines.append(
        "> Retrieved from [Microsoft Customer Stories]"
        "(https://www.microsoft.com/en/customers/)\n"
    )
    lines.append(f"Total matching stories: {total_count}\n")
    lines.append("---\n")

    for i, card in enumerate(cards, 1):
        content = card.get("content", {})
        title = content.get("title", "Untitled")
        slug = card.get("name", "")
        url = get_story_url(slug) if slug else ""

        industries = content.get("industries", [])
        industry_text = (
            ", ".join(ind.get("text", "") for ind in industries)
            if industries
            else "N/A"
        )

        products_list = (
            content.get("footer", {})
            .get("relatedProducts", {})
            .get("products", [])
        )
        products_text = (
            ", ".join(p.get("label", "") for p in products_list)
            if products_list
            else "N/A"
        )

        lines.append(f"## Story {i}: {title}\n")
        lines.append(f"**URL:** [{url}]({url})\n")
        lines.append(f"**Industry:** {industry_text}\n")
        lines.append(f"**Related Products:** {products_text}\n")

        quotes = content.get("quotes", [])
        if quotes:
            for quote in quotes:
                if isinstance(quote, dict):
                    quote_text = quote.get("text", "")
                    quote_author = quote.get("author", "")
                    if quote_text:
                        lines.append(f'> *"{quote_text}"*')
                        if quote_author:
                            lines.append(f"> — {quote_author}")
                        lines.append("")
                elif isinstance(quote, str) and quote:
                    lines.append(f"> {quote}\n")

        lines.append("---\n")

    return "\n".join(lines)


@app.route(route="MyHttpTrigger", auth_level=func.AuthLevel.FUNCTION)
def MyHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    product = req.params.get('product')
    if not product:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            product = req_body.get('product')

    if not product:
        return func.HttpResponse(
            "Please pass a product name on the query string"
            " or in the request body"
            " (e.g., product=Azure Functions).",
            status_code=200,
        )

    try:
        data = search_customer_stories(product)
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch customer stories: {e}")
        return func.HttpResponse(
            "Failed to fetch customer stories from the API."
            " Please try again later.",
            status_code=500,
        )

    cards = data.get("cards", [])
    if not cards:
        return func.HttpResponse(
            f"No customer stories found for '{product}'.",
            status_code=200,
        )

    result = format_stories(product, data)
    return func.HttpResponse(result, status_code=200, mimetype="text/plain")