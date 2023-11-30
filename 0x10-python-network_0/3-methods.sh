#!/bin/bash
# This disolays the http requests the server will accept
curl -sI  "$1" | sed -n '/Allow: /s/Allow: //p'
