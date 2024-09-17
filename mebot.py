from transformers import GPT2LMHeadModel, GPT2Tokenizer

def respone(query):
    # Load the tokenizer and model from the directory where you saved them
    model_dir = "D:/stud bot/model"  # Replace with the path to the downloaded model folder

    tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
    model = GPT2LMHeadModel.from_pretrained(model_dir)

    # Generate text to evaluate the model
    input_text = query
    inputs = tokenizer(input_text, return_tensors="pt")

    # Generate text with the model
    outputs = model.generate(
        inputs['input_ids'],
        max_length=100,
        num_return_sequences=1,
        do_sample=True, 
        top_k=50,
        top_p=0.95
    )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text
