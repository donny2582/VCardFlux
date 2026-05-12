# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
import re

class VCardJSONInput(BaseModel):
    lastName: str = Field(..., example="黃")
    firstName: str = Field(..., example="峻翊")
    org: Optional[str] = Field(None, example="高手國際股份有限公司")
    title: Optional[str] = Field(None, example="數據分析師兼總統")
    tel_work: Optional[str] = Field(None, example="0220772077")
    tel_cell: Optional[str] = Field(None, example="0966556633")
    email: Optional[str] = Field(None, example="408650033@thi.com.tw")
    # vCard ADR 格式: [postbox, extended, street, locality, region, code, country]
    # 格式順序：[郵政信箱, 擴充地址, 街道, 城市, 省份/縣市, 郵遞區號, 國家]
    adr: List[str] = Field(
        default=["", "", "", "", "", "", ""], 
        example=["PO Box 123", "10樓之5", "中正路38號", "士林區", "臺北市", "111", "中華民國"],
        min_items=7, max_items=7
    )
    note: List[str] = Field(
        default=["", "", ""], 
        description="專長或備註清單",
        example=["數據視覺化", "Python自動化", "交通大數據"]
    )
    url: Optional[str] = Field(None, example="www.gov.tw")

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if v and not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", v):
            raise ValueError("Email 格式不正確")
        return v
        
    @field_validator('tel_work', 'tel_cell')
    @classmethod
    def validate_phone(cls, v):
        if v and not re.match(r"^[\d\+\-\(\)\s]+$", v):
            raise ValueError("電話號碼格式不正確，只能包含數字與部分符號")
        return v
        
    @field_validator('adr')
    @classmethod
    def validate_adr(cls, v):
        if len(v) != 7:
            raise ValueError("地址(adr)陣列必須剛好包含 7 個元素")
        return v

    @property
    def full_name(self):
        return f"{self.lastName}{self.firstName}"