import datetime

def hello_world(name="World"):
    if not name:
        name = "World"
    return f"Hello, {name}!"

def hello_multiple(*names):
    if not names:
        return "Hello, World!"
    greetings = [f"Hello, {name}!" for name in names]
    return "\n".join(greetings)

def hello_with_time(name="World"):
    current_time = datetime.datetime.now().strftime("%H:%M")
    return f"Hello, {name}! Current time is {current_time}"

if __name__ == "__main__":
    print(hello_world())
    print(hello_with_time("Alice"))