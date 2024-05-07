import asyncio
import time 

async def brewCoffee():
    print("Coffee Brewing")
    await asyncio.sleep(4)
    print("Coffee Brewed")
    # Notify the user that the coffee is ready
    return "Coffee Ready"

async def toastBread():
    print("Bread Toasting")
    await asyncio.sleep(3)
    print("Bread Toasted")
    # Notify the user that the bread is ready
    return "Bread Ready"

async def main():
    print("loading")
    start_time = time.time()
    
    batch = asyncio.gather(brewCoffee(), toastBread())
    result_coffee, result_bread = await batch

    end_time = time.time()

    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBread: {result_bread}")
    # Print the time taken to complete the task
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

asyncio.run(main())
