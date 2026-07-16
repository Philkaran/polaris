#!/bin/bash
echo "Hostname: $(hostname)"
echo "User: $(whoami)"
echo "Date: $(date)"
echo "Disk usage:"
df -h / | tail -1
