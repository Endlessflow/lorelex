# Lorelex : Study Smart. Not Hard.

## Introduction

This project stems from the recognition that the modern learner's journey is fraught with distractions, inefficiencies, and manual processes. In the age of advanced AI and automation, we have the tools to make this journey smoother and more enjoyable. This project is about harnessing the power of Large Language Models (LLMs) and other software tools to streamline, and potentially automate, the redundant processes involved in knowledge acquisition, consolidation, and retrieval.


## Current Manual Workflow

#### Acknowledgements

This workflow was derived from the prompts and workflow presented in [Jake Romm](https://www.youtube.com/@JakeRommMD)'s video [How to make better flashcards with GPT-3.5 (Anki Flashcards)](https://www.youtube.com/watch?v=-8jF2hw3FiY). Shoutout to Jake for these amazing prompts he shared with the community.

### Preparation

**Personalization of Prompts**:
- Before diving into the regular workflow for a new class or subject, take a moment to customize the `Prompt2` and `Prompt3`.
- Adjust these prompts based on the nature of the subject or class. For instance, for 'Software Engineering', you could modify `Prompt2` to highlight programming concepts, software design patterns, and differentiation between similar algorithms.
- This ensures that when you do engage with the AI, the prompts are primed for extracting the most relevant information for your learning goals.

### Regular Workflow

1. **Segmentation of Reference Material**:
    - Divide your reference material into manageable chunks suitable for ChatGPT. 
    - Find the right balance: too little information may miss context, while too much can compromise the output's quality.

2. **Concept Explanation**:
    - Use `Prompt1` in ChatGPT to elucidate specific concepts.
    - Insert the segmented section from the reference material into `Prompt1`.
    - Engage in a Q&A with the AI for deeper understanding, if necessary.

3. **Information Extraction**:
    - Use the personalized `Prompt2` in ChatGPT to extract crucial information.
    - Insert either the segmented section from the referenve material or the chunked output derived from prior steps into `Prompt2`.
    - Repeat as necessary, especially if new insights emerge from step 2.

4. **Flashcard Generation**:
    - Use the personalized `Prompt3` in ChatGPT to craft flashcards in a markdown table format.
    - Insert the list of filtered information from step 3 into `Prompt3`.
    - Copy the generated table to your spreadsheet software of choice.

5. **Rince and Repeat**:
    - Repeat steps 2-4 for all topics and subtopics.
    - When done, export the spreadsheet as a `.csv` file.

6. **Memory Retention**:
    - Import the `.csv` into Anki or a similar flashcard application to periodically review and reinforce the knowledge.

#### Example
See an example of the prompts in action here : https://chat.openai.com/share/82a11fa5-8afe-4c24-8faa-c2d8585863ec.


## Short-term goals

1. **Workflow Enhancement**:
    - Identify repetitive or time-consuming steps in the current workflow that can be streamlined.
    - Experiment with different configurations of the ChatGPT prompts to optimize information extraction and understanding.

2. **Integration Scripts**:
    - Develop scripts or tools to automate the transfer of data between the reference material, ChatGPT, the spreadsheet software and Anki (e.g. Aim to reduce manual copy-pasting between different tools, possibly through browser extensions or direct integrations. This alone could save significant time and energy.)
    - Test these tools for bugs and improve user experience.

3. **Keep the code documented and clean**
   - Document the code and periodically review it to ensure clarity and ease of use.


## Future Milestones

1. **Knowledge Organization Phase**:
    - Once the minimum workflow is perfected, begin the process of integrating a digital "second brain" to store and organize knowledge.
    - This phase will provide a structured system for learners to organize, link and retrieve information.

2. **Standalone Tool Creation**:
    - Finish developping basic tools for each of the different steps in the learning workflow.
    - Ensure these tools individually address the specific challenges and bottlenecks of the workflow.

3. **Integration Phase**:
    - Combine the standalone tools into a cohesive, streamlined workflow with a solution allowing chaining the standalone tools seamlessly.
    - Enable an interface where learners can upload materials and undergo the entire learning, storage, linking and flashcard creation process with minimal manual interaction focusing only on learning and pondering. 
