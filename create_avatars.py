import os

# Create simple SVG avatars
avatars = [
    ('#667eea', '#764ba2', '😊', 'avatar1'),
    ('#f093fb', '#f5576c', '😎', 'avatar2'), 
    ('#4facfe', '#00f2fe', '🤓', 'avatar3'),
    ('#43e97b', '#38f9d7', '😄', 'avatar4'),
    ('#fa709a', '#fee140', '🙂', 'avatar5'),
    ('#a8edea', '#fed6e3', '😍', 'avatar6')
]

os.makedirs('static/images', exist_ok=True)

for color1, color2, emoji, name in avatars:
    svg_content = f'''<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad{name}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color1};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{color2};stop-opacity:1" />
    </linearGradient>
  </defs>
  <circle cx="50" cy="50" r="50" fill="url(#grad{name})" />
  <text x="50" y="65" font-family="Arial, sans-serif" font-size="36" fill="white" text-anchor="middle">{emoji}</text>
</svg>'''
    
    # Save as SVG
    with open(f'static/images/{name}.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f'Created {name}.svg')

print('Avatar SVG files created successfully!')
