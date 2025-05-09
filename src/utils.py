import os
import json
import yaml
from dotenv import load_dotenv
import google.generativeai as genai
from Configs.prompts import creative_brief_prompt_template
from src.models import UserInput


load_dotenv()


def load_config() -> dict:
    with open("Configs/config.yaml", "r") as f:
        return yaml.safe_load(f)


def initialize_gemini():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    config = load_config()
    return genai.GenerativeModel(config["model"])


def search_searxng(query, method='GET'):
    # Example stubbed search result to simulate actual web search
    result = (
        "ECCO was established in 1963 by Karl Toosbuy"
        " in the small town of Bredebro "
        "in southern Denmark. Throughout the 1980s, "
        "the company expanded its operations "
        "internationally. By 1982, sales reached"
        " 1 million pairs of shoes annually. "
        "To meet demand, ECCO added production"
        " in Portugal, Japan, and Cyprus. "
        "ECCO built its R&D center 'Futura' in 1996, "
        "with Portugal becoming its main R&D hub by 2009. "
        "They opened a beamhouse in Indonesia and tannery"
        " in Thailand. In 1998, ECCO launched its "
        "first flagship retail store on Oxford Street, London. "
        "By 2000, ECCO controlled all production stages."
    )
    return result


def websearch(query):
    return search_searxng(query, method='GET')


def extract_search_data(results, max_results=5):
    if not results or 'results' not in results:
        return "No relevant information found."

    search_data = []
    for i, result in enumerate(results.get('results', [])):
        if i >= max_results:
            break

        title = result.get('title', '')
        url = result.get('url', '')
        content = result.get('content', '')

        if title and content:
            search_data.append(
                f"Source: {title}\nURL: {url}\nContent: {content}"
            )

    return "\n\n".join(search_data)


def generate_creative_brief(user_input: UserInput) -> dict:
    try:
        model = initialize_gemini()

        search_query = (
            f"{user_input.brand_name} {user_input.product_name} marketing campaign"
        )
        search_results = websearch(search_query)

        brand_info = ""
        if search_results:
            brand_info = extract_search_data(search_results)
        else:
            print("No search results found or search failed")

        enhanced_input = user_input.dict()
        enhanced_input["web_research"] = brand_info

        prompt = creative_brief_prompt_template.format(
            user_input=json.dumps(enhanced_input, indent=2)
        )

        response = model.generate_content(prompt)
        content = response.text.strip()

        if content.startswith("```json"):
            content = content[7:-3].strip()

        return json.loads(content)
    except Exception as e:
        return {"error": str(e)}
