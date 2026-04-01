from app.agents.router.schema import RouterInput, Route
from app.agents.router.classifier import RouterClassifier

class RouterAgent:
    def __init__(self):
        self.classifier = RouterClassifier()
    
    def run(self, input_data: RouterInput) -> Route:
        route = self.classifier.classify(input_data.question)

        if route == "tool":
            return Route.TOOL
        
        if route == "rag":
            return Route.RAG
        
        return Route.CHAT

        

