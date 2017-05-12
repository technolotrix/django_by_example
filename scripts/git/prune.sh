BRANCH=$1

git checkout master
git pull origin master
git remote prune origin
git branch -D $BRANCH
