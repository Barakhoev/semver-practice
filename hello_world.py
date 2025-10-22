def hello_world(name="World"):
    if not name:
        name = "World"
    return f"Hello, {name}!"

def hello_multiple(*names):
    if not names:
        return "Hello, World!"
    greetings = [f"Hello, {name}!" for name in names]
    return "\n".join(greetings)