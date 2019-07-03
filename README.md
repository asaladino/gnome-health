# Gnome Health
A health data monitoring app for gnome. Organize and collect all
your health data into one location.

## Build

### Compile Resources

```
cd ./src/resources/
glib-compile-resources --target=gnome-health.gresource gnome-health.gresource.xml
```

## References

### Sample App
OfflineImap is a good example of a python app packaged with snap.

https://github.com/snapcraft-docs/offlineimap/blob/master/setup.py

### Snap Docs
Instructions on packaging an app for snap.

https://docs.snapcraft.io/python-apps

### Pony ORM
Documentation on using PonyORM.

https://docs.ponyorm.org/firststeps.html