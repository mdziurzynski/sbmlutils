# remove unnecessary files
find .. -type f -regex '.*pyc' | xargs rm
find .. -type f -regex '.*class' | xargs rm
find .. -type f -regex '.*~' | xargs rm
