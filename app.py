from flask import Flask

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Handle the incoming webhook data
    return 'Webhook received'  # Optionally, send a response

if __name__ == '__main__':
    app.run()
