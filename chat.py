from huggingface_hub import InferenceClient
import os



client = InferenceClient(token="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")

print("Instructions:\n Use /imagine to generate an image (/image 'promt')\n Use /stop to stop the conversation\n")
print("Hello how can I help you?")

promt = ""
imageCount = 0

while(promt != "/stop"):
    promt = input()

    if promt.startswith("/imagine"):
        
        try:
            client = InferenceClient(model="stabilityai/stable-diffusion-xl-base-1.0",
                                      token="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")
            
            client.headers["x-use-cache"] = "0"

            newPromt = promt[len("/imagine"):].strip()
            answer = client.text_to_image(newPromt, guidance_scale=9)

            image_path = os.path.join(os.getcwd(), f"image_{imageCount}.png")
            answer.save(image_path)
            
            imageCount += 1
            print("Your image is ready! How can I help you now?")

        except Exception as e:
            print(f"Sorry, I’m having trouble generating this image. Can you imagine something else?{e}")
    


    else:
        try:

            client = InferenceClient(model="nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
                                      token="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")
            

            answer = client.text_generation(prompt=promt,
                                            temperature=0.7,
                                            max_new_tokens=4000,
                                            repetition_penalty=1.2)
            print(answer)

        except:
            print("Sorry, I don’t understand your question. Could you please ask again?")


print("Thank you for using me!")