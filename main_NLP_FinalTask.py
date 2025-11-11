import subprocess

def ask_model(prompt):
    command = [
        '/main', # file in lama.cpp folder
        '-m', './models/mistral.gguf', # path to the model
        '-p',  prompt,
        '--temp', '0.3' # The value that controls the hallucination
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE)
    return result.stdout.decode()

if __name__ == "__main__":
    print("Local LLM CLI")
    while True:
        question = input(">> ")
        if question.lower() in ["exit", "quit"]:
            break
        print(ask_model(question))