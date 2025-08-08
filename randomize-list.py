import random
import time

def detect_signal():
    print('detecting...')
    with open('randomize-list.txt', 'r') as f:
        cards = f.readlines()
        if cards != '':
            handle_request(cards)

def handle_request(data):
    print('handling request...')
    cards = shuffle_cards(data)
    send_response(cards)

def shuffle_cards(cards):
    print('randomizing cards...')
    random.shuffle(cards)
    return cards

def send_response(cards):
    print('sending cards...')
    with open('randomize-list.txt', 'w') as f:
        for card in cards:
            f.write(card)

while True:
    detect_signal()
    time.sleep(5)
