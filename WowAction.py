from Action import *

response = '''וווואווווווווו😱😱😱😱😱
אתם לא מאמינים זה אשכרה עובד!!! אם תגידו את המשפט שכתוב פה למטה שלוש פעמים ותשתפו לחמש קבוצות אתם לא תאמינו מה קורה!!!!!!!!!!!!!!!! האייקון של הדיסקורד יהפוך לאדום‼️‼️‼️‼️

אַשְהַדֻ אַן לַא אִלָהַ אִלַּא אללָּה וַאַן מֻחַמַּדַ(ן) רַסוּלֻ אללָּה.

כדאי לכם ממממשששש לנסות לי זה עבד וזה ממש מגניבב🤭🤭🤭'''


class WowAction(Action):
    def __init__(self):
        super().__init__("")

    def should_respond(self, message, client):
        return client.user.mentioned_in(message) and message.content.replace(" ", "").replace("<@!" + str(client.user.id) + ">", '') == "wow"

    async def do_action(self, message, client, discord):
        return response, True
