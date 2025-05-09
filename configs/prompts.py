creative_brief_prompt_template = """
You are a senior marketing strategist and copywriter. Based on the following user input, generate a **detailed and properly structured creative brief** formatted as a **valid JSON object**.

---

**User Input:**
{user_input}

---
**Instructions:**
1. Use the web research information to inform your creative brief with relevant details about the brand and product.
2. Include any relevant events, key dates, or market trends found in the research.
4. Do **not** include placeholder text like "TBD" or "N/A" unless absolutely necessary.
5. Use markdown-safe, plain text strings (no rich text formatting).

Use the structure below to format the brief. Ensure each section is completed with clear, relevant, and original content. Do **not** include placeholder text like "TBD" or "N/A" unless absolutely necessary. Use markdown-safe, plain text strings (no rich text formatting).

---

**JSON Structure Required:**
```json
{{
  "title": "",
  "campaign_name": "",
  "objective": "",
  "target_audience": {{
    "demographics": "",
    "psychographics": "",
    "additional": ""
  }},
  "deliverables": {{
  "content": [
    {{
      "platform": "",
      "content_type": "",
      "duration": "",
      "description": "",
      "posting_requirements": ""
    }}
   ]
  }},
  "content_requirements": {{
    "do": [],
    "dont": []
  }},
  "key_insights": {{
    "text": "",
    "cite": []
  }},
  "brand_positioning": "",
  "core_message": "",
  "tagline": "",
  "creative_approach": {{
  "approaches": [{{"id": "", "approach": ""}}]
  }},
  "success_metrics": [{{"key": "", "value": ""}}],
  "events": [
    {{
      "name": "",
      "date": "",
      "location": "",
      "description": "",
      "registration_link": "",
      "organizer": "",
      "highlights": "[]"
    }}
  ],
  "disclaimer": "",
  "usage_permissions_and_brand_exclusivity": {{
    "description": "",
    "social_media_usage_duration": "",
    "paid_media_duration": "",
    "offline_advertising_permission": "",
    "exclusivity_duration": "",
    "terminology": {{
      "whitelisting": "",
      "derivative_works": "",
      "boosted_paid_media": "",
      "dark_posting": ""
    }}
  }},
  "call_to_action": "",
  "brief_id": ""
}}"""
