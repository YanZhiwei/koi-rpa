import json
from dataclasses import asdict, dataclass


@dataclass(init=False)
class Boss:
    name: str = ""
    title: str = ""
    active_state: str = ""

    def to_jon(self):
        return json.dumps(self.to_dict(), default=str)

    def to_dict(self):
        return asdict(self)
