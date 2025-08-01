'''
OPTIONAL AI GUIDANCE PROMPT:
----------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions to
a practice problem that my professor gave me to try before class. Please be my
kind tutor and walk me through how to solve the problem step by step.

Don't just give me the full solution all at once (unless I later ask for it).
Instead, help me work through it gradually, with clear explanations and small,
easy-to-understand examples. Please use everyday language and explain things
in a simple, friendly way.


INSTRUCTIONS:
-------------
In your pantry you currently have 10 apples. Your friend just came back to the 
apartment with more apples. Ask them how many apples they bought, and then
calculate the new total.

1. Ask the user how many apples they brought home.
2. Convert that number from the input() function into an integer.
3. Print a message with the total of the original 10 apples and the new amount
   added together, for example: "You now have a total of <new number> apples."
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

current_apples = 10
new_apples = input("How many apples did you bring? ")
new_apples = int(new_apples) # you could do this on the line above too

print(f"You now have a total of {current_apples + new_apples} apples.")
