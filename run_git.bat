cd C:\Users\ishan\Documents\Projects\Awesome-Federated-Learning

git --git-dir=.git --work-tree=. add .
git --git-dir=.git --work-tree=. commit -m "detailed pages created"
git --git-dir=.git --work-tree=. push

git --git-dir=.git --work-tree=. add .
git --git-dir=.git --work-tree=. commit --allow-empty -m "seo optimised and decorated"
git --git-dir=.git --work-tree=. push

python update_readme.py

git --git-dir=.git --work-tree=. add .
git --git-dir=.git --work-tree=. commit -m "star history added"
git --git-dir=.git --work-tree=. push

git --git-dir=.git --work-tree=. add .
git --git-dir=.git --work-tree=. commit --allow-empty -m "fixed star plot"
git --git-dir=.git --work-tree=. push

git --git-dir=.git --work-tree=. add .
git --git-dir=.git --work-tree=. commit --allow-empty -m "invalid awesome link fixed"
git --git-dir=.git --work-tree=. push
