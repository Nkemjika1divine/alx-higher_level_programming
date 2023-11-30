#!/bin/bash
# Sends a request tio a url and returns statud cide only
curl -sw '%{http_code}' -o /dev/null "$1"
