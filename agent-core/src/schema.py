from pydantic import BaseModel, Field
from typing import Optional, List

class CondoListing(BaseModel):
    """
    Structured data extracted from a condo listing page.
    Includes both 'Hard Data' (explicit facts) and 'Soft Data' (Agent inference).
    """
    # Basic Info (Hard Data)
    address: str = Field(description="Full address of the condo unit.")
    price: float = Field(description="Listing price in CAD.")
    sqft: Optional[str] = Field(description="Square footage range or exact value.")
    maintenance_fees: Optional[float] = Field(description="Monthly maintenance fees/condo fees.")
    
    # The "Hard" Criteria
    bedrooms: int = Field(description="Number of bedrooms.")
    bathrooms: int = Field(description="Number of bathrooms.")
    parking_included: bool = Field(description="True if listing explicitly mentions owned or assigned parking.")
    locker_included: bool = Field(description="True if listing explicitly mentions owned or assigned locker.")
    
    # The "Soft" / LLM Analysis
    exposure_direction: Optional[str] = Field(description="N, S, E, W, SW, etc. derived from description.")
    view_description: Optional[str] = Field(description="Summary of view (e.g., 'CN Tower view', 'Lake view', 'Facing brick wall').")
    renter_ratio_risk: Optional[str] = Field(description="Assessment of if the building seems investor-heavy vs owner-occupied based on listing tone.")
    
    # Location Intelligence
    nearby_amenities: List[str] = Field(default=[], description="Specific mentions of 'Martin Goodman Trail', 'High Park', etc.")
    distance_to_trail_km: Optional[float] = Field(description="Distance to nearest bike/walking trail.")
    distance_to_water_km: Optional[float] = Field(description="Distance to lake or kayak launch point.")
    
    # The Verdict
    investment_score: int = Field(description="Score 1-10 based on value, layout, and view.")
    reasoning: str = Field(description="Why you gave this score.")
