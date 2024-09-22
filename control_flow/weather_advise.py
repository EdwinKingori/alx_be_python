current_weather = input("What's the weather like today? (sunny/rainy/cold): ")

if current_weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif current_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
elif current_weather == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
else:
    print("Sorry, I don't have recommendations for this weather.")
