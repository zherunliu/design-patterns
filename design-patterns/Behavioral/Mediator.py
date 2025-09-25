from typing import Dict

# from sys import stdin


# mediator
class ChatRoomMediator:
    def __init__(self) -> None:
        self.users: Dict[str, ChatUser] = {}

    def add_user(self, user: "ChatUser"):
        self.users[user.name] = user

    def send_message(self, sender: str, message: str):
        for user in self.users.values():
            if user.name != sender:
                user.receive_message(sender, message)


# component
class ChatUser:
    def __init__(self, name: str, mediator: ChatRoomMediator) -> None:
        self.name = name
        self.mediator = mediator
        self.received_message: Dict[str, str] = {}

    def send_message(self, message: str):
        self.mediator.send_message(self.name, message)

    def receive_message(self, sender: str, message: str):
        self.received_message[sender] = message
        print("%s received: %s" % (self.name, message))


if __name__ == "__main__":
    n = int(input())
    users_name = input().split()
    mediator = ChatRoomMediator()
    for name in users_name:
        user = ChatUser(name, mediator)
        mediator.add_user(user)

    # # sys.stdin
    # for line in stdin:
    #     if not line:
    #         continue
    #     sender, message = line.split()
    #     user = mediator.users.get(sender)
    #     if user:
    #         user.send_message(message)

    # try... except EOFError...
    while True:
        try:
            sender, message = input().split()
            user = mediator.users.get(sender)
            if user:
                user.send_message(message)
        except EOFError:
            break
