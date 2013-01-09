for dir in ./cmsplugin_*
do
  (cd $dir && echo $dir && django-admin.py compilemessages)
done
