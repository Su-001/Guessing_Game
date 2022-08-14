secret_word = "cat"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False
name = input("ENTER YOUR NAME : ")
print("hint : it's an animal ")

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit-1:
        guess = input("enter guess: ")
        guess_count += 1

    elif guess_count <guess_limit :
         print("want hints? Y/N ")
         hints =input("Y/N")
         if hints == "Y" or "y":
            print("Hint : three letter word")
            guess = input("enter guess: ")
            guess_count += 1
         else :
            guess = input("enter guess: ")
            guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses :
    print(name +  "are out of guesses," +name+ " lose! ")
else:
    print(name + " win")
