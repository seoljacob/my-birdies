import os

def get_env_var(s):
   return os.getenv(s).split(",")

def days_to_list(s):
    match s:
        case "m":
            return ["Monday"]
        case "w":
            return ["Wednesday"]
        case "mw":
            return ["Monday", "Wednesday"]
        case _:
            return []

def guests_to_list(s):
    return s.split("+")
