from dataclasses import dataclass 

@dataclass
class Message:
    value: bytes
    key: bytes