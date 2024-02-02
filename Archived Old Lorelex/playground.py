import keyboard
import clipboard
import os



def load_template_from_file( file_path: str):
    """
    Load the template from a file and set it with the specified name and temperature.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No file found at: {file_path}")
    
    name = os.path.splitext(os.path.basename(file_path))[0]
    with open(file_path, 'r') as file:
        template = file.read()
    
    return template

def handle_template_clipboard_injection():
    FILENAME = "markdown_mini_lecture_generator"
    current_dir = os.path.dirname(__file__)
    prompts_dir = os.path.join(current_dir, "prompts")
    file_path = os.path.join(prompts_dir, f"{FILENAME}.txt")
    
    clipboard_content = clipboard.paste()
    print(clipboard_content)
    template = load_template_from_file(file_path)
    clipboard.copy(template.format(source_material=clipboard_content))

# open the prompts directory



keyboard.add_hotkey('ctrl+alt+1', handle_template_clipboard_injection)

keyboard.wait()














exit()
from OpenAIChat import OpenAIChat
import os

current_dir = os.path.dirname(__file__)
prompts_dir = os.path.join(current_dir, "prompts")

source_material = """38
Interface
▪ Une interface est un contrat
▪ Elle spécifie un ensemble de
méthodes sans les implémenter
▪ La classe implémentant l’interface
doit implémenter toutes les
méthodes définies par cette
interface
▪ Elle ne peut être instanciée
« Interface »
Personne
+ getAge (): Nombre
Homme
+ getAge (): Nombre"""

chat = OpenAIChat()

chat.load_template_from_file(os.path.join(prompts_dir, "extract_info_ING150.txt"), temperature=0)
chat.load_template_from_file(os.path.join(prompts_dir, "remove_analogies_ING150.txt"), temperature=1)
formating_template = """Please reorganize the following information in the <extracted> tags into a list of coherent verbose pieces of information. Each piece of information should stand on its own and represent a complete idea or concept.

<extracted>
{text_to_reorganize}
</extracted>
"""
chat.set_template("formating_ING150", formating_template, temperature=1)


extracted_info = chat.get_response("extract_info_ING150", verbose=True, text_to_parse=source_material)
filtered_info = chat.get_response("remove_analogies_ING150", verbose=True, text_to_analyze=extracted_info)
formatted_info = chat.get_response("formating_ING150", verbose=True, text_to_reorganize=filtered_info)

exit()

print("*****************************************************************")
print("*****************************************************************")
print("*****************************************************************")
print("*****************************************************************")


extracted_info = chat.get_response("extract_info_ING150", verbose=True, text_to_parse=source_material)
filtered_info = chat.get_response("remove_analogies_ING150", verbose=True, text_to_analyze=extracted_info)

alternative_all_in_one_extract_template = """Given the extracted text from a lecture's powerpoint on physics, please rephrase and elaborate to extract factual, definitional, or principial information clearly and concisely. Ensure to convert the content into complete, coherent, and grammatically correct sentences, organized in a list format. 

Extracted Text:
"{extracted_text}"

Please generate a list of clear and concise factual, definitional, or principial information based on the extracted text.

"""

chat.set_template("alternative_all_in_one_extract_ING150", alternative_all_in_one_extract_template, temperature=1)
formatted_info = chat.get_response("alternative_all_in_one_extract_ING150", verbose=True, extracted_text=source_material)




"""42
Polymorphisme d’héritage
▪ Le polymorphisme d’héritage
▪ Lié aux notions d’héritage et d’interface
▪ Les sous-classes redéfinissent (override) certaines
méthodes de la superclasse pour implémenter leur
comportement spécifique
▪ Une classe implémente toutes les méthodes définies par
l’interface qu’elle implémente"""

"""Couplage
▪ Analogie du monde réel (couplage faible)
▪ Imagine utiliser des blocs de construction
magnétiques pour créer différentes structures.
▪ Chaque composant de la structure est indépendant
et peut être facilement détaché sans affecter le reste
de la construction.
▪ Si on veut modifier une partie spécifique, comme
ajouter une aile supplémentaire à l'avion, il faut
simplement retirer l'aile existante et ajouter la
nouvelle, sans avoir à toucher le reste de l'avion.
▪ C'est un exemple de couplage faible, car les
composants (blocs) sont indépendants et facilement
interchangeables"""


"""29
Couplage
▪ Qu’est-ce que c’est?
▪ Pourquoi faut-il le minimiser?
▪ Couplage: mesure de dépendances entre classes
▪ Un couplage minimisé facilite:
▪ La compréhension des classes
▪ La maintenance
▪ Limiter l’effet des changements d’une classe sur les autres
classes du système
▪ La réutilisation des classes"""


"""26
Héritage
▪ Relation d’héritage: « est »
▪ Une sous-classe est un cas particulier de la
superclasse
▪ Permet la réutilisation des états et du
comportement d’une classe générale
par une classe plus spécialisée
▪ La classe générale définit un ensemble de
propriétés communes à des classes plus
spécialisées
▪ La classe plus spécialisée peut définir des
propriétés additionnelles qui lui sont propres
Animal
son
…
getSon (): String
….
Chien
race
…
getRace(): String
…
"""

step1_template = """Extract and list all factual, definitional, or principial information related to software engineering from the provided <text>.

<text>
{input}
</text>
"""

step2_template = """From the extracted information from the provided <extracted>, reorganize the extracted information into a list of concise, standalone bullet points. Each bullet point should present a complete thought and mention the subject of the statement.

<extracted>
{step1_extraction}
</extracted>
"""

step3_template = """From the extracted information from the provided <extracted>, remove any examples, analogies, or illustrative content that is not presenting empirical facts or foundational knowledge.

<extracted>
{step2_extraction}
</extracted>
"""

step4_template = """From the bullet list of extracted information provided in <extracted>, review each bullet point in a vacuum. Then, ensure clarity and conciseness while maintaining completeness of thought by correcting any bullet point that would be ambiguous or unclear.


<extracted>
{step3_extraction}
</extracted>
"""

