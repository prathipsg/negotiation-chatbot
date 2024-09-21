def negotiation_logic(user_offer, starting_price=100):
    min_price = 50  # Lowest price the chatbot will accept
    if user_offer >= starting_price:
        return f"I accept your offer of ${user_offer}!"
    elif user_offer < starting_price and user_offer >= min_price:
        return f"How about ${user_offer + 10}? I can offer a discount!"
    else:
        return "Sorry, I can't go that low."
