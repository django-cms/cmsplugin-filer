# -*- coding: utf-8 -*-


def rename_tables(db, table_mapping, reverse=False):
    """
    renames tables from source to destination name, if the source exists and the destination does
    not exist yet.
    """
    from django.db import connection
    if reverse:
        table_mapping = [(dst, src) for src, dst in table_mapping]
    table_names = connection.introspection.table_names()
    for source, destination in table_mapping:
        if source in table_names and destination in table_names:
            print(u"    WARNING: not renaming {0} to {1}, because both tables already exist.".format(source, destination))
        elif source in table_names and destination not in table_names:
            print(u"     - renaming {0} to {1}".format(source, destination))
            db.rename_table(source, destination)


def rename_tables_old_to_new(db, table_mapping):
    return rename_tables(db, table_mapping, reverse=False)


def rename_tables_new_to_old(db, table_mapping):
    return rename_tables(db, table_mapping, reverse=True)
