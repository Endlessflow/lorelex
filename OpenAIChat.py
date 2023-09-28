import os
import openai

class OpenAIChat:
    def __init__(self, api_key: str = os.getenv("OPENAI_API_KEY"), model: str = "gpt-3.5-turbo"):
        openai.api_key = api_key
        self.model = model
        self.templates = {}
        
    def set_template(self, name: str, template: str, temperature: float = 0.7):
        """
        Set the template with placeholders and optional parameters.
        """
        self.templates[name] = {
            "template": template,
            "temperature": temperature
        }
        
    def load_template_from_file(self, file_path: str, temperature: float = 0.7):
        """
        Load the template from a file and set it with the specified name and temperature.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No file found at: {file_path}")
        
        name = os.path.splitext(os.path.basename(file_path))[0]
        with open(file_path, 'r') as file:
            template = file.read()
        
        self.set_template(name, template, temperature)
        
    def get_response(self, template_name: str, verbose: bool = False, **kwargs) -> str:
        """
        Fill the template with provided field values and get a response from the API.
        """
        if template_name not in self.templates:
            raise ValueError(f"No template found with the name: {template_name}")
        
        template = self.templates[template_name]["template"]
        temperature = self.templates[template_name]["temperature"]
        filled_template = template.format(**kwargs)
        
        # Create a system message to initiate the conversation
        messages = [{"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": filled_template}]
        
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=temperature
        )
        
        response = completion.choices[0].message['content']
        
        if verbose:
            print("Filled Template:", filled_template)
            print("API Response:", response)
        
        return response

exit()

# EXAMPLE USECASE

STARTING_CONTENT = """42
Polymorphisme d’héritage
▪ Le polymorphisme d’héritage
▪ Lié aux notions d’héritage et d’interface
▪ Les sous-classes redéfinissent (override) certaines
méthodes de la superclasse pour implémenter leur
comportement spécifique
▪ Une classe implémente toutes les méthodes définies par
l’interface qu’elle implémente"""

if __name__ == "__main__":
    chat = OpenAIChat()

    # Load templates from files
    chat.load_template_from_file("prompts/prompt2.txt")
    chat.load_template_from_file("prompts/prompt3.txt")

    # Get a response from the API by filling the template
    extracted_info = chat.get_response("prompt2", verbose=True, reference_material=STARTING_CONTENT)

    # Get another response from the API by filling another template
    flashcards = chat.get_response("prompt3", verbose=True, text_to_transform=extracted_info)
