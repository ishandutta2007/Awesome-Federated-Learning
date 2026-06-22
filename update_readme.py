import os

base_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Federated-Learning"
readme_path = os.path.join(base_dir, 'README.md')

with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

# Add Star History
star_history = """
## ⭐️ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-Federated-Learning&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Federated-Learning&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Federated-Learning&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Federated-Learning&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
if "## ⭐️ Star History" not in readme:
    readme += "\n" + star_history

# Replace chartrepos with chart?repos
readme = readme.replace('chartrepos', 'chart?repos')

# Replace awesome link
readme = readme.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)
