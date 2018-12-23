from dialogue_manager import DialogueManager
from utils import RESOURCE_PATH

class SimpleDialogueManager(object):
    """
    This is the simplest dialogue manager to test the telegram bot.
    Your task is to create a more advanced one in dialogue_manager.py."
    """

    def generate_answer(self, question):
        return "Hello, world!"


def main():
    dialogue_mgr = DialogueManager(RESOURCE_PATH)

    print("I'm ready!")

    while True:
        query = input()
        answer = dialogue_mgr.generate_answer(query)
        print(answer)



if __name__ == "__main__":
    main()
