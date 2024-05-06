import time 

def brewCoffee():
    print("Coffee Brewing")
    time.sleep(2)
    print("Coffee Ready")
    # Notify the user that the coffee is ready
    return "Coffee Ready"

def toastBread():
    print("Bread Toasting")
    time.sleep(4)
    print("Bread Ready")
    # Notify the user that the bread is ready
    return "Bread Ready"

def main():
    start_time = time.time 
    
    result_coffee = brewCoffee()
    result_bread = toastBread()

    end_time = time.time

    print(f"")

    print(f"Time taken: {end_time - start_time}")

    if __name__ == "__main__":
        main()