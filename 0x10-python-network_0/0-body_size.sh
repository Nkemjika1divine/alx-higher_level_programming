#!/bin/bash
# This script curls body size
curl -sw '%{size_download}\n' -o /dev/null "$1"
