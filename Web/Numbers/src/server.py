from flask import Flask, request, render_template_string
import random
import time

app = Flask(__name__)

def generate_seed():
    return int(time.time() // 3)  # Updates seed every 5 seconds

# Route for the CTF challenge
@app.route('/', methods=['GET', 'POST'])
def challenge():
    seed = generate_seed()
    random.seed(seed)

    flag = 'dscctf{1_4m_4_m47h5_3xp3r7_w17h_c0d1n6_5k1ll5!}'
    num1 = random.randint(10000, 999999)
    num2 = random.randint(10000, 999999)

    answer = num1 + num2

    if request.method == 'POST':
        user_answer = request.form['answer']
        try:
            user_answer = int(user_answer)
            if user_answer == answer:
                return render_template_string(f'<p>{flag}</p>')
            else:
                return 'Incorrect. Try again.'
        except ValueError:
            return 'Invalid input. Please enter a number.'

    return render_template_string("""
    <h1>What is {{ num1 }} + {{ num2 }}?</h1>
    <form method="POST">
        <input type="text" name="answer" placeholder="Your answer" required>
        <button type="submit">Submit</button>
    </form>
    """, num1=num1, num2=num2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=36082)
