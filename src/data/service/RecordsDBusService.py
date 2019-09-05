import dbus

from src.data.model.Record import Record
from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository
from src.utility.DbSession import create_session


# Sample Server Object
# https://github.com/LEW21/pydbus/blob/master/examples/clientserver/server.py
class RecordsDBusService(object):
    """
    <node>
        <interface name='com.codingsimply.Health'>
            <method name='create'>
                <arg type='a{sv}' name='record' direction='in'/>
                <arg type='b' name='response' direction='out'/>
            </method>
        </interface>
    </node>
    """

    # @dbus.service.method(dbus_interface='com.codingsimply.Health.Records', in_signature='o', out_signature='o')
    # https://stackoverflow.com/questions/16741057/d-bus-d-feet-send-dictionary-of-string-variants-in-python-syntax
    # {
    #     'type': GLib.Variant("i", 1),
    #     'source_name': GLib.Variant("s", 'test function'),
    #     'source_version': GLib.Variant("s", '1.0.1'),
    #     'unit': GLib.Variant("s", 'in'),
    #     'created': GLib.Variant("s", "2019-09-27 19:01:47 -0400"),
    #     'start': GLib.Variant("s", "2019-09-27 19:01:47 -0400"),
    #     'end': GLib.Variant("s", "2019-09-27 19:01:47 -0400"),
    #     'value': GLib.Variant("i", 265),
    # }
    @staticmethod
    def create(record):
        record_to_insert = Record.build_from_dict(record)
        with RecordsSqliteRepository(create_session()) as repo:
            repo.save(record_to_insert)
        return True
