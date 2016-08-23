for dir in ./cmsplugin_*
do
  (cd $dir && echo $dir && django-admin.py makemessages -l en)
done
