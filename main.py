"""Module to connect to a test server and parse the output"""

import paramiko


def connect_to_server():
    """
    Connect to the remote server
    """
    try:
        server = "18.139.113.249"
        test_account = "practest"
        test_password = "tAFsQ7QsAhmDfdCG"
        client = paramiko.SSHClient()
        policy = paramiko.AutoAddPolicy()
        client.set_missing_host_key_policy(policy)
        client.connect(server, username=test_account, password=test_password)
        return client
    except Exception as exception:
        print(type(exception).__name__)
        return None


def get_command_output(server_connection, command: str) -> str:
    """
    Execute a command on the server
    """
    _stdin, stdout, _stderr = server_connection.exec_command(command)
    return stdout.read().decode()


def main():
    server_connection = connect_to_server()
    if not server_connection:
        print("Could not connect to the server")
        return

    # Example to execute command on remote server,
    command_output = get_command_output(server_connection, "ls")
    print(command_output)

    # Insert your code here

    server_connection.close()


if __name__ == "__main__":
    main()
