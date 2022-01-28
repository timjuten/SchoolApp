import socket

server = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM

)

server.bind(
    ("127.0.0.1", 6578)
)

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

