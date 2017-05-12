BRANCH=$1

git checkout master
git pull origin master
git checkout -b $BRANCH
git push --set-upstream origin $BRANCH