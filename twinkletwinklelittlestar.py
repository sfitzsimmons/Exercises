# A project to show knowledge of text formatting
# The goal is to print this long string out formatted with new lines and tabs

sample_string = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!"

# I would just use triple quotes, but the assignment wants me to use /n and /t for new line and tab

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")

# here's how I'd do it:

print('''
Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky
Twinkle, twinkle, little star,
    How I wonder what you are!''')
