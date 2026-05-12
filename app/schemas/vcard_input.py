from pydantic import BaseModel, Field
from typing import List, Optional

class VCardJSONInput(BaseModel):
    lastName: str = Field(..., example="黃")
    firstName: str = Field(..., example="翔龍")
    org: Optional[str] = Field(None, example="高手國際股份有限公司")
    title: Optional[str] = Field(None, example="數據分析師")
    tel_work: Optional[str] = Field(None, example="0220772077")
    tel_cell: Optional[str] = Field(None, example="0966556633")
    email: Optional[str] = Field(None, example="408650033@thi.com.tw")
    # vCard ADR 格式: [postbox, extended, street, locality, region, code, country]
    adr: List[str] = Field(
        default=["", "", "", "", "", "", ""], 
        min_items=7, max_items=7
    )
    note: List[str] = Field(
        default=["", "", ""], 
        description="專長或備註清單",
        example=["專長一", "專長二", "專長三"]
    )
    url: Optional[str] = Field(None, example="www.gov.tw")

    @property
    def full_name(self):
        return f"{self.lastName}{self.firstName}"