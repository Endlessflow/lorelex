import keyboard
import clipboard
from DataManager import DataManager

SUMMARIZER = "I think I understand now. Can you tie everything we talked about together into one explanation ?\nHowever,  make sure to optimize for word economy - imagine that each word you said was very expensive and you were a very frugal person."

# Global DataManager instance
data_manager = DataManager()


# Hotkey functions
def handle_update_reference_material():
    data_manager.modify_reference(clipboard.paste())


def handle_update_extracted_info():
    data_manager.modify_extracted_info(clipboard.paste())


def handle_load_prompt1():
    clipboard.copy(data_manager.prompt1)


def handle_load_prompt2():
    clipboard.copy(data_manager.prompt2)


def handle_load_prompt3():
    clipboard.copy(data_manager.prompt3)


# Set up global hotkeys
keyboard.add_hotkey('ctrl+alt+4', handle_update_reference_material)
keyboard.add_hotkey('ctrl+alt+5', handle_update_extracted_info)
keyboard.add_hotkey('ctrl+alt+1', handle_load_prompt1)
keyboard.add_hotkey('ctrl+alt+2', handle_load_prompt2)
keyboard.add_hotkey('ctrl+alt+3', handle_load_prompt3)

# Keep the script running
keyboard.wait()
