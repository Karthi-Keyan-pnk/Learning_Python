import tomllib

with open("config.toml", "rb") as f:
    tomldata: dict = tomllib.load(f)

print(tomldata)
