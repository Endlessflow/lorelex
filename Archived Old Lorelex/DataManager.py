import os

class DataManager:
    def __init__(self):
        # Initial data
        self.reference_material = ""
        self.extracted_info = ""
        
        # Store the original templates
        self._template1 = self.load_template("prompt1.txt")
        self._template2 = self.load_template("prompt2.txt")
        self._template3 = self.load_template("prompt3.txt")

        # Initial prompts
        self.prompt1 = self._template1
        self.prompt2 = self._template2
        self.prompt3 = self._template3
        
    def load_template(self, filename):
        with open(os.path.join("prompts", filename), "r") as f:
            return f.read()

    def modify_reference(self, new_reference):
        self.reference_material = new_reference
        self.update_prompts_using_reference()

    def modify_extracted_info(self, new_info):
        self.extracted_info = new_info
        self.update_prompts_using_extracted_info()

    def update_prompts_using_reference(self):
        self.prompt1 = self._template1.replace("<reference>\n\n</reference>", f"<reference>\n{self.reference_material}\n</reference>")
        self.prompt2 = self._template2.replace("<reference>\n\n</reference>", f"<reference>\n{self.reference_material}\n</reference>")

    def update_prompts_using_extracted_info(self):
        self.prompt3 = self._template3.replace("<text>\n\n</text>", f"<text>\n{self.extracted_info}\n</text>")

# Usage:
data_manager = DataManager()

# Later in the script, when you modify the reference or extracted info:
data_manager.modify_reference("New Reference Material")
data_manager.modify_extracted_info("New Extracted Info")

print(data_manager.prompt1)
print(data_manager.prompt2)
print(data_manager.prompt3)
