
from flask import Request

from lib.config import Environment

class Paging:
  page: int
  per_page:int
  
  def __init__(self, page:int, per_page:int):
    self.page = page
    self.per_page = per_page

def extract_paging_http_request(request: Request):
    per_page = int(request.args.get(
        "per_page", Environment.api_paging_default_per_page))
    page = int(request.args.get("page", Environment.api_paging_default_page))
    return Paging(per_page=per_page, page=page)
