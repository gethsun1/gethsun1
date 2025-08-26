#!/usr/bin/env python3
"""
Simple snake animation generator for GitHub contributions
"""

import requests
import json
from datetime import datetime, timedelta
import os

def generate_snake():
    # Get user's contribution data
    username = "gethsun1"
    url = f"https://api.github.com/users/{username}/events"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            events = response.json()
            
            # Create a simple snake SVG
            svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="120" viewBox="0 0 1000 120">
  <defs>
    <linearGradient id="snakeGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D4FF;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#FF6B6B;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#4ECDC4;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Background -->
  <rect width="100%" height="120" fill="#0D1117"/>
  
  <!-- Title -->
  <text x="50%" y="25" text-anchor="middle" fill="#00D4FF" font-family="monospace" font-size="18" font-weight="bold">🐍 Contribution Snake</text>
  <text x="50%" y="45" text-anchor="middle" fill="#FFFFFF" font-family="monospace" font-size="12">Eating your commits one day at a time!</text>
  
  <!-- Snake body -->
  <g transform="translate(50, 80)">
    <!-- Snake path -->
    <path d="M 0 0 Q 100 -30 200 0 Q 300 30 400 0 Q 500 -30 600 0 Q 700 30 800 0 Q 900 -30 1000 0" 
          stroke="url(#snakeGradient)" stroke-width="4" fill="none" stroke-linecap="round"/>
    
    <!-- Snake head -->
    <circle cx="1000" cy="0" r="12" fill="#00D4FF"/>
    <circle cx="1005" cy="-5" r="3" fill="#FFFFFF"/>
    <circle cx="1005" cy="-5" r="1.5" fill="#000000"/>
    
    <!-- Snake eyes -->
    <circle cx="1008" cy="-8" r="2" fill="#FFFFFF"/>
    <circle cx="1008" cy="-8" r="1" fill="#000000"/>
    <circle cx="1008" cy="8" r="2" fill="#FFFFFF"/>
    <circle cx="1008" cy="8" r="1" fill="#000000"/>
    
    <!-- Contribution squares (simplified) -->
    <rect x="50" y="-10" width="8" height="8" fill="#00D4FF" opacity="0.8"/>
    <rect x="150" y="-10" width="8" height="8" fill="#FF6B6B" opacity="0.8"/>
    <rect x="250" y="-10" width="8" height="8" fill="#4ECDC4" opacity="0.8"/>
    <rect x="350" y="-10" width="8" height="8" fill="#00D4FF" opacity="0.8"/>
    <rect x="450" y="-10" width="8" height="8" fill="#FF6B6B" opacity="0.8"/>
    <rect x="550" y="-10" width="8" height="8" fill="#4ECDC4" opacity="0.8"/>
    <rect x="650" y="-10" width="8" height="8" fill="#00D4FF" opacity="0.8"/>
    <rect x="750" y="-10" width="8" height="8" fill="#FF6B6B" opacity="0.8"/>
    <rect x="850" y="-10" width="8" height="8" fill="#4ECDC4" opacity="0.8"/>
    <rect x="950" y="-10" width="8" height="8" fill="#00D4FF" opacity="0.8"/>
  </g>
</svg>'''
            
            # Ensure output directory exists
            os.makedirs('output', exist_ok=True)
            
            # Write SVG file
            with open('output/github-contribution-grid-snake-dark.svg', 'w') as f:
                f.write(svg_content)
            
            print("Snake generated successfully!")
            return True
            
    except Exception as e:
        print(f"Error generating snake: {e}")
        return False

if __name__ == "__main__":
    generate_snake()
