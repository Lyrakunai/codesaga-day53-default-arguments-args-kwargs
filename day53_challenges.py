
# Codesaga - Day 53
# Mini Challenges

#-------------------------------------------
# Challenge 1: Flexible Expense Entry System
#-------------------------------------------

def add_expense(name, *tags, amount=0, **details):
    expense = {
        "name": name,
        "amount": amount,
        "tags": tags,
        "details": details
    }

    print("\n--- Expense Details ---")
    print("Name:", expense["name"])
    print("Amount:", expense["amount"])
    print("Tags:", expense["tags"])
    print("Additional Information:", expense["details"])


add_expense(
    "Grocery",
    "food",
    "home",
    amount=850,
    payment_method="UPI",
    location="Gaya",
    month="August",
    note="Monthly grocery"
)

add_expense(
    "Notebook",
    "study",
    "stationery",
    payment_method="cash",
    location="Patna"
)



#--------------------------------------------
# Challenge 2: AI Model Configuration Builder
#--------------------------------------------

def create_model_config(model_name, *capabilities, temperature=0.7, **options):
    config = {
        "model": model_name,
        "temperature": temperature,
        "capabilities": capabilities,
        "options": options
    }

    print("\n--- AI Model Configuration ---")
    print("Model:", config["model"])
    print("Temperature:", config["temperature"])
    print("Capabilities:", config["capabilities"])
    print("Additional Options:", config["options"])


create_model_config(
    "VisionModel",
    "text_generation",
    "vision",
    "tool_use",
    temperature=0.3,
    max_tokens=2000,
    language="English",
    streaming=True
)

create_model_config(
    "TextModel",
    "text_generation",
    temperature=0.7,
    max_tokens=1000,
    streaming=False
)
