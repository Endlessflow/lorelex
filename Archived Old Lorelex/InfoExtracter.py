from OpenAIChat import OpenAIChat
import os
import os
from pdfminer.high_level import extract_text
from datetime import datetime

def initialize_chat():
    chat = OpenAIChat()
    current_dir = os.path.dirname(__file__)
    prompts_dir = os.path.join(current_dir, "prompts")
    chat.load_template_from_file(os.path.join(prompts_dir, "extract_info_LOG121.txt"), temperature=0)
    chat.load_template_from_file(os.path.join(prompts_dir, "remove_analogies_LOG121.txt"), temperature=1)
    chat.load_template_from_file(os.path.join(prompts_dir,"formating_info.txt"), temperature=1)
    return chat

def get_filtered_info(source_material, chat):
    extracted_info = chat.get_response("extract_info_LOG121", verbose=True, text_to_parse=source_material)
    filtered_info = chat.get_response("remove_analogies_LOG121", verbose=True, text_to_analyze=extracted_info)
    formatted_info = chat.get_response("formating_info", verbose=True, text_to_reorganize=filtered_info)
    return formatted_info




# Function to extract text from a PDF and format it into markdown
def extract_to_markdown(pdf_path: str, output_folder: str, chat: str):
    # Extract text using pdfminer
    text = extract_text(pdf_path)
    
    # Create markdown content
    markdown_content = []
    
    # Add YAML Front Matter
    markdown_content.append("---")
    markdown_content.append(f"title: '{os.path.basename(pdf_path)}'")
    markdown_content.append(f"date: {datetime.today().strftime('%Y-%m-%d')}")
    markdown_content.append("script: pdf_extractor")
    markdown_content.append(f"source: {os.path.basename(pdf_path)}")
    markdown_content.append("---")
    
    # Split text by page and format in markdown
    pages = text.split("\x0c")  # PDFs often use Form Feed (\x0c) as a page separator
    for i, page in enumerate(pages):
        if page.strip():  # To ensure we don't add empty pages
            markdown_content.append(f"## Page {i+1}/{len(pages)}")
            
            # Extract text from page
            extracted = get_filtered_info(page, chat)

            markdown_content.append(extracted)

            markdown_content.append("---")  # Page separator in markdown
            
            # Write to markdown file
            markdown_filename = os.path.basename(pdf_path).replace('.pdf', '.md')
            with open(os.path.join(output_folder, markdown_filename), 'a', encoding="utf-8") as f:
                f.write("\n".join(markdown_content))
            
            # Clear markdown content for next page
            markdown_content.clear()

    # Write final markdown content to file
    #with open(os.path.join(output_folder, markdown_filename), 'a', encoding="utf-8") as f:
    #    f.write("\n".join(markdown_content))
    
    # Clear markdown content
    #markdown_content.clear()


# Main execution
if __name__ == "__main__":
    input_folder = "PDFs"
    output_folder = "extracted_info"

    chat = initialize_chat()

    if not os.path.exists(input_folder):
        os.mkdir(input_folder)
        print(f"Initialised an empty folder at ./{input_folder} please run the script again with PDFs in the folder")
        exit()

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for pdf_file in os.listdir(input_folder):
        if pdf_file.endswith(".pdf"):
            extract_to_markdown(os.path.join(input_folder, pdf_file), output_folder, chat)
