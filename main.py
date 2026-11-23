# One-Star Review of Something Essential
import os

out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, 'entry.txt'), 'w', encoding='utf-8') as f:
    f.write("The sun wakes you up for free every morning and immediately begins fading your curtains.")