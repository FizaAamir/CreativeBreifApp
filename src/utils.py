import os
import json
import yaml
import requests
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
    # config = load_config()
    # url = config.get("searxng_url", "http://127.0.0.1:8081/search")
    
    # params = {
    #     'q': query,
    #     'format': 'json'
    # }
    # headers = {
    #     'User-Agent': '"User-Agent": "Mozilla/5.0 (compatible; GeminiBot/1.0)"'
    # }

    # try:
    #     print(f"Searching for: {query} using {method} method.")
    #     if method.upper() == 'POST':
    #         response = requests.post(url, data=params, headers=headers)
    #     else:
    #         response = requests.get(url, params=params, headers=headers)
        
    #     if response.status_code != 200:
    #         print("Error response content:\n", response.text)
    #         return None
    result = "ECCO was established in 1963 by Karl Toosbuy in the small town of Bredebro in southern Denmark. Throughout the 1980s, the company expanded its operations internationally. By 1982, sales reached 1 million pairs of shoes annually. In order to accommodate the increasing demand, additional production was established in Portugal, and under license in Japan and Cyprus.[2] ECCO built its own research and design center, named 'Futura', in Denmark in 1996, since 2009 Portugal is the R&D center of ECCO and opened its own beamhouse in Indonesia and tannery in Thailand a few years later. In 1998 the first flagship retail store opened on Oxford Street, in London. By 2000, ECCO owned every step of the production process, from design and leather production to branded retail sales."
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
            search_data.append(f"Source: {title}\nURL: {url}\nContent: {content}")
    
    return "\n\n".join(search_data)

def generate_creative_brief(user_input: UserInput) -> dict:
    try:
        model = initialize_gemini()
        
        search_query = f"{user_input.brand_name} {user_input.product_name} marketing campaign"
        search_results = websearch(search_query)
        
        brand_info = ""
        if search_results:
            brand_info = extract_search_data(search_results)
        else:
            print("No search results found or search failed")
        
        enhanced_input = user_input.dict()
        enhanced_input["web_research"] = brand_info
        
        prompt = creative_brief_prompt_template.format(user_input=json.dumps(enhanced_input, indent=2))

        response = model.generate_content(prompt)
        
        content = response.text.strip()
        if content.startswith("```json"):
            content = content[7:-3].strip()
        
        return json.loads(content)
    except Exception as e:
        return {"error": str(e)}

