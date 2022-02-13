import socket
from school_project.User.data import get_user

server = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM


)

server.bind(

    
    ("127.0.0.1", 1234) # localhost

)

server.listen(5)

limit = 10
users = {server}
user_count = 0


while True:
    user_socket, address = server.accept()
    user_socket.send("You're connected".encode("utf-8"))
    user_count += 1
    print(f"Користувач {user_socket} під'єднався. {user_count}/10")
    if len(users) > limit:
        users.remove(server)
        server.close()
        print("Сервер заповнений")


    class voteCreator:
        def __init__(self, email):
            self.email = email
            self.user = get_user(self.email)

        def check_role(self):
            if self.user[5] == "вчитель" or self.user[5] == "директор" or self.user[5] == "куратор":
                print("Чудово, ви можете створити голосування")
                return True
            else:
                print("Вибачте, ви не можете створити голосування")
                return False
                
        def create_vote(self):

            name_msg = user_socket.send("Введіть назву голосування: ".encode("utf-8"))
            body_msg = user_socket.send("Введіть опис голосування: ".encode("utf-8"))
            self.name = user_socket.recv(2048).decode("utf-8")
            self.body = user_socket.recv(2048).decode("utf-8")

            user_socket.send(f'Почалося голосуання з назвою "{self.name}" та описом "{self.body}"'.encode("utf-8"))

        def vote(self):
            user_socket.send(f'Почалося голосуання з назвою "{self.name}" та описом "{self.body}"\n Напишіть Y якщо так, або N якщо ні'.encode("utf-8"))
            answer = user_socket.recv(2048).decode("utf-8")
            

            yes_count = 0
            no_count = 0
            if answer == "y".lower():
                yes_count += 1
                
            elif answer == "n".lower():
                no_count += 1

            if yes_count > no_count:
                percent = (yes_count/(yes_count + no_count)) * 100
                print(f'{round(percent)}% обрали "Так"')

            elif yes_count < no_count:
                percent = (no_count/(yes_count + no_count)) * 100
                print(f'{round(percent)}% обрали "Ні"')

    data = user_socket.recv(2048)
    vote_creator = voteCreator(data.decode("utf-8"))
    role = vote_creator.check_role()
    if role:
        vote_creator.create_vote()

    vote_creator.vote()
    

    

    
    




user_count = 0
LIMIT = 10

server.listen(5)
print("Server is running")

while True:
    user_socket, address = server.accept()
    user_count += 1
    if user_count == LIMIT:
        server.close()

    print(f"{user_socket} підключився. {user_count}/10")

    user_socket.send("Вітаю".encode("utf-8"))


