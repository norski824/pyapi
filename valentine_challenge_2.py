import json
  
def main():
    with open("challenge.json", "r") as json_data:
        json_read_data = json_data.read()

        #print(json_read_data)

        json_to_python = json.loads(json_read_data)

        for person in json_to_python:
            print(person["name"])
            print(person["eyeColor"])
            print(person["favoriteFruit"])    



if __name__ == "__main__":
        main()
