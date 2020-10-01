echo "========Git: add -> commit -> push========="

git add *
git ls-files --other --modified --exclude-standard
git commit -m "A BAT file committed on %date%-%time%"
git push