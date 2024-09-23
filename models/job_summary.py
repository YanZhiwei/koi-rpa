import json
from dataclasses import asdict, dataclass
from typing import List


@dataclass(init=False)
class JobSummary:
    id: str = ""
    name: str = ""
    url: str = ""
    company: str = ""
    area: str = ""
    tags: List[str] = None
    salary: str = ""
    language: str = ""

    def to_jon(self):
        return json.dumps(self.to_dict(), default=str)

    def to_dict(self):
        return asdict(self)
