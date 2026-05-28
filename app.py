from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

while True:
    user=input("you :")

    if user == "exit":
        break

    prompt= f"""
<|system|>
you are a helpful assistant.
<|user|>
{user}
<|assistant|>
"""
    
    result = pipe(
        prompt,
        max_new_tokens=100
    )

    generated = result[0]["generated_text"]

    answer = generated[len(prompt):]

    print(answer)
