# import openai library
import openai

# Set up the OpenAI API client
openai.api_key = "PUT_YOUR_API_KEY"

# this loop will let us ask questions continuously and behave like ChatGPT
while True:
    # Set up the model and prompt
    engine_model_gpt3 = "text-davinci-003"
    
    prompt = input('Enter new prompt: ')

    if prompt in ['exit','quit','salir','terminar']:
        break

    # Generate a response
    completion = openai.Completion.create(
        engine=engine_model_gpt3,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.3,
    )

    # extracting useful part of response
    response = completion.choices[0].text
    
    # printing response
    print(response)