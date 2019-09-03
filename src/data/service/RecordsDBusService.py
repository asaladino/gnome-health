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
    				<arg type='o' name='record' direction='in'/>
    				<arg type='o' name='response' direction='out'/>
    			</method>
    		</interface>
    	</node>
    """

    # def __init__(self, object_path):
    #     dbus.service.Object.__init__(self, dbus.SessionBus(), object_path)

    # @dbus.service.method(dbus_interface='com.codingsimply.Health.Records', in_signature='o', out_signature='o')
    def create(self, record):
        record_to_insert = Record()
        with RecordsSqliteRepository(create_session()) as repo:
            record_to_insert.copy_from_object(record)
            repo.save(record_to_insert)
        return record_to_insert
