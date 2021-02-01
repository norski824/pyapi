import json

def main():
    with open("challenge.json", "r") as json_data:
        json_read_data = json_data.read()

        #print(json_read_data)

        json_to_python = json.loads(json_read_data)

        print(json_to_python[3]['name'], json_to_python[3]['eyeColor'], json_to_python[3]['favoriteFruit'])
            

if __name__ == "__main__":
        main()
