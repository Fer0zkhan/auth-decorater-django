from django.contrib import admin


def set_admin(_class, search_fields: tuple, ordering: tuple, list_display: tuple):
    class_name = _class.__name__ + 'Admin'
    Meta = type('Meta', (object,), {'model': _class})

    AdminClass = type(class_name,
                      (admin.ModelAdmin,),
                      {
                          'Meta': Meta,
                          'search_fields': search_fields,
                          'ordering': ordering,
                          'list_display': list_display
                          # "sayHello": lambda self: "Hi, I am " + self.name
                      }
                      )
    admin.site.register(_class, AdminClass)
    return AdminClass
