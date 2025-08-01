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
You are organizing teams for a campus escape room event. You want to print
a formatted list of team members using special escape sequences.

1. Create a variable for the team name.
2. Create variables for the names of 3 team members.
3. Print a message with the team name, followed by each member's name on a
   new line using \n. Make each team member's name indented by adding \t
   Example:
   "Team: Code Crackers\n\tAlice\n\tBen\n\tCarla"
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

team_name = "Puzzle Masters"
member_1 = "Tyler"
member_2 = "Rachel"
member_3 = "Sam"

print(f"Team: {team_name}\n\t{member_1}\n\t{member_2}\n\t{member_3}")
