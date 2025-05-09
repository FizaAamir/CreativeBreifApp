from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class UserInput(BaseModel):
    brand_name: str
    product_name: str
    personas: Dict[str, Any]
    brand_guidelines: Dict[str, Any]
    web_research: Optional[str] = Field(default="", description="Information gathered from web search")

class CreativeBrief(BaseModel):
    title: str
    campaign_name: str
    objective: str
    # Define other fields if needed...
