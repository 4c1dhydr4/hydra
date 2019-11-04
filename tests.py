# import database as db
from blackhydra import Hydra

hydra = Hydra('hydra')

print(hydra.read_serial())
# hydra.post_twitter('Testing v2.0')
hydra.send_text_to_me('Test')
hydra.display_logs()