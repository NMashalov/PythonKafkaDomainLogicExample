import requests

class RegistryScheme:
    def __init__(self,base_url:str, topic_name: str):
        self.base_url = base_url
        self.topic_name = topic_name 
    
    def get_scheme(self):
        r = requests.get(
            f'{self.base_url}/subjects/{self.topic_name}/versions/latest'
        )
        if r.status_code != 200:
            raise Exception('Schema retrieval failed')
        return r