import sys
import os
import yaml
import flask
from envconfig import CONFIG

app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)


class Person(object):
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(f"{format_string}: {person.name}")
    #print(format_string.format(person=person))


def fetch_website(urllib_version, url):
    # Import the requested version (2 or 3) of urllib
    if urllib_version != "2" or urllib_version != "3":
        print("Not allowed")
        return

    exec(f"import urllib{urllib_version} as urllib", globals())
    # Fetch and print the requested URL

    try:
        http = urllib.PoolManager()
        r = http.request('GET', url)
    except:
        print('Exception')


def load_yaml(filename):
    #stream = open(filename)
    #deserialized_data = yaml.load(stream, Loader=yaml.Loader) #deserializing data
    with open(filename) as stream:
        deserialized_data = yaml.safe_load(stream, Loader=yaml.Loader) #deserializing data
    return deserialized_data

def authenticate(password):
    # Assert that the password is correct
    #assert password == "Iloveyou", "Invalid password!"
    if password == "iloveyou":
        print("Successfully authenticated!")
    else:
        print("Wrong password")

if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    if sys.version_info[0] == 2:
        input = raw_input

    choice  = input("Select vulnerability: ")
    if choice == "1":
        new_person = Person("Vickie")
        print_nametag(input("Please format your nametag: "), new_person)
    elif choice == "2":
        urlib_version = input("Choose version of urllib: ")
        fetch_website(urlib_version, url="https://www.google.com")
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)

