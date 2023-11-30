#!/bin/bash
# This sends a POST request to a yrl and displays tge response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
