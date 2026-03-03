from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class TagTemplateBase(BaseModel):
    part_id: int
    template_layout: Optional[str] = None
    fields_required: Optional[str] = None


class TagTemplateCreate(TagTemplateBase):
    pass


class TagTemplateUpdate(BaseModel):
    template_layout: Optional[str] = None
    fields_required: Optional[str] = None


class TagTemplateRead(TagTemplateBase):
    tag_template_id: int
    last_updated: Optional[datetime] = None

    model_config = {"from_attributes": True}
