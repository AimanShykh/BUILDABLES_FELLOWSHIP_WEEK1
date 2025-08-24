from transformers import AutoTokenizer

tokenizer1 = AutoTokenizer.from_pretrained("gpt2")
tokenizer2 = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "This assignment is part of Buildables Fellowship"


tokens1 = tokenizer1.tokenize(text)
tokens2 = tokenizer2.tokenize(text)

print("Gpt2 Tokens:", tokens1, len(tokens1))
print("Bert Tokens:", tokens2, len(tokens2))


cost_per_1k_tokens = 0.03 #for gpt 4
estimated_cost_gpt2 = (8 / 1000) * cost_per_1k_tokens
print(f"Estimated Cost (GPT-2 equivalent): ${estimated_cost_gpt2:.6f}")