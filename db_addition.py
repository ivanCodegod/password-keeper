from tqdm import tqdm
from time import sleep

help_list = {
    'intro': f"Welcome to <<Password keeper program>>\nIn this program you can store your passwords for easy or get "
             f"it back.",
    'commands': f"\nAVAILABLE COMMANDS\n{'-' * 50}\n'get' - To get your information that you "
                f"already save.\n'set' - To set your information into a storage.\n'all' - To see all "
                f"Title's.\n'q' To quit the program.\n'comm' - To see all available commands.\n{'-' * 50}",
    'help_propose': "\nWrite 'coom' To see all commands\nWrite 'q' to quit",

}


def progress_bar():
    for _ in tqdm(range(2)):
        sleep(1)
