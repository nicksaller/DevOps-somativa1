import yaml

with open("hello_world.yaml", "r") as f:
    hello_world = yaml.load(f, Loader=yaml.FullLoader)

print(hello_world[0])
