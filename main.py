import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer',
     }
     {
         'name':'Ricardo',
         'company': 'Facebook',
         'email': 'ricardo@facebook.com',
         'position': 'Date enginee',
     }      
]

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in client\'s list')
        
def list_clients():
    for idx, client in enumerate(clients):
        print('{uid}│{name}│{company}│ {email}│{position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))

def update_client(client_name, update_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients [index] = updated_name
    else:
         print('Client not in clients\'s list')
         
def delete_client(client_name):
    global clients

    if client_name in clients:
        clients remove(client_name)
    else:
        print('Client  not in clients\'s list')

def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field   

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')

        if client_name == 'exit':
            client_name = None
            break
     if not client_name:
         sys.exit()

     return client_name    



def _print_Welcome():
    print('Welcome TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _print_Welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name':_get_client_field('name'),
            'company':_get_client_field('company'),
            'email': _get_client_field('email'),
            'position':_get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_name = input('What is the new client naame? ')

        updated_client(client_name, updated_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name')
        update_client(client_name, update_client_name)
        list_clients()
         if found:
          print("The client in in the clients list")

       else :
          print('The client: {} is not on our clients list ', format(client_name))
 
    else:
        print('Invalid command')