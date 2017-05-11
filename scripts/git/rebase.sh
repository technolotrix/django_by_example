BRANCH=$1

git checkout master
git pull origin master
git checkout $BRANCH
git rebase master
git push -f origin $BRANCH
