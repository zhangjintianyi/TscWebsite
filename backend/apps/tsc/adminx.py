from backend.extra_apps import xadmin
from backend.apps.tsc.models import MSO, TSC, DBS


class MSOAdmin(object):
    list_display = ["mso_id", "ip", "department", "port",
                    "unit_type", "version", "setup_time", "principal"]
    search_fields = ["mso_id", "ip"]


class TSCAdmin(object):
    list_display = ["tsc_id", "ip", "department", "port", "carrier_num",
                    "unit_type", "version", "setup_time", "principal", "tsc_type", "mso"]
    search_fields = ["tsc_id", "ip"]


class DBSAdmin(object):
    list_display = ["ip", "department", "port", "unit_type", "version",
                    "setup_time", "principal", "dbs_type", "mso"]
    search_fields = ["tsc_id", "ip"]


xadmin.site.register(MSO, MSOAdmin)
xadmin.site.register(TSC, TSCAdmin)
xadmin.site.register(DBS, DBSAdmin)
