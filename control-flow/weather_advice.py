user_input = input("What's the weather like today? (sunny/rainy/cold): ")

if user_input == "sunny":
  print("Wear a t-shirt and sunglasses.")
elif user_input == "rainy":
  print("Don't forget your umbrella and a raincoat.")
elif user_input == "cold":
  print("Make sure to wear a warm coat and a scarf.")
else:
  print("I don't have a recommendation for this weather.")