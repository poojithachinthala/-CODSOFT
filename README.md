# -CODSOFT
Tasks and projects for CODSOFT Internship
✅ Task 1: Rule-Based Chatbot (CODSOFT Internship)

## 📌 Description
A simple yet advanced rule-based chatbot built using Python.  
It responds to user inputs using pattern matching and predefined rules, simulating a basic conversational experience.

## ✅ Features
- Pattern matching with regular expressions (`re`)
- Class-based design for clean structure
- Random default responses for unknown queries
- Covers greetings, help, jokes, and more

## 🚀 How to Run
1. Clone or download this repo
2. Open terminal in project directory
3. Run: `python chatbot.py`
4. Chat with the bot!

## 💡 Sample Inputs
- hello / hi / hai
- how are you
- tell me a joke
- who made you
- bye

## 🧠 Technologies Used
- Python 3
- Regular Expressions (`re` module)


✅ Task 2: Tic-Tac-Toe AI (tic_tac_toe.py)
📌 Description
A Python-based terminal game where the human player (X) plays against an unbeatable AI (O) powered by the Minimax algorithm with Alpha-Beta Pruning. The AI always plays optimally, ensuring it never loses.

💡 Features
🤖 AI decision-making using Minimax algorithm

⚡ Faster performance with Alpha-Beta Pruning

🎨 Colored terminal output using colorama
(X = Red, O = Green)

🧮 Score Tracking across multiple rounds (You, AI, Ties)

🔁 Option to replay the game after each match

✅ Fully terminal-based, no extra UI

▶️ How to Run
bash
Copy
Edit
# Step 1: Install colorama (only once)
pip install colorama

# Step 2: Run the game
python tic_tac_toe.py
🎮 How to Play
The game displays a 3x3 board like this:

Copy
Edit
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Enter the number (1–9) to place your X

The AI (O) will instantly respond with its move

After each round, you'll see:

Who won or if it was a tie

Updated score

Option to play again (y/n)

📊 Example Output
mathematica
Copy
Edit
| 1 | 2 | 3 |
| 4 | X | 6 |
| O | 8 | 9 |

AI is making a move...

| 1 | 2 | 3 |
| 4 | X | O |
| O | 8 | 9 |

😔 You lost! AI wins.
Score: You - 0 | AI - 1 | Ties - 0
Play again? (y/n):
🧠 Technologies Used
Tool	Purpose
Python 3	Core programming language
colorama	Colored terminal output
Minimax	AI decision-making algorithm
Alpha-Beta Pruning	Optimizes Minimax




