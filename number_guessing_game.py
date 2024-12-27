import random

def is_number(num) :
    try:
        float(num)
        return True
    except TypeError:
        return False

while True :
    print("Enter the suggested number. Make sure you don't make more than five mistakes in a row or you will be game over.")
    
    print("Select the starting number for the guess interval:")
    start_num = int(input())
    print("Choose the end number for the guess interval:")
    end_num = int(input())
    
    if start_num > end_num :
        
        raise Exception("The ending number must be greater than the starting number.")
    
    else :
        
        random_num = int(random.randrange(start_num, end_num))
        
        for i in range(5) :
            if i <= 3 :
                print(f"Write the {i + 1} number you guessed:")
            else :
                print("Guess the last number, otherwise you are game over:")
            
            guess_num = int(input())
            
            if is_number(guess_num) :
                pass
            else :
                print("TypeError called")
            
            if random_num == guess_num :
                print(f"Well done, you guessed right. {random_num} is the estimated number.")
                break
            else :
                if i <= 3 :
                    print("You guessed wrong. Try again.")
                else :
                    print("Game Over!")