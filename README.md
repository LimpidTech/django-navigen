# django navigen
#### Brandon R. Stoner <monokrome@monokro.me>

## What is this?

This application provides components that simplify the creation of dynamic navigation menus in django. You can use to to have django automatically generate menus with menu items that reflect the permissions of the currently logged in user.

## Getting started

Just like other django apps, django-navigen is really easy to get started with. Simply install it with:

    python setup.py install

After this is installed, open up your project's settings.py file and add 'navigen' to your INSTALLED_APPS.

    INSTALLED_APPS = (
        # Your other apps listed here
        'navigen',
    )

Now, as a final step - have django synchronize your database:

    ./manage.py syncdb

## How does this work?

You should now have all that you need to use django-navigen within your application. In order to test this it is good to know the terminology used by the navigation system or you might be confused or think that the application is overly complicated. However, remember that django-navigen was made with the following goals in mind:

* All menus are generated dynamically
* Menu items reflect the context of the user, and their related permissions. Users shouldn't see what they can't access.
* The application should support as many dynamic menus as required by the design out-of-the-box.
* Drop-down menus should be easily created without any extra code.

These are established by organizing each menu as a *"navigation tree"*, and relating each tree's top-level *"menu items"* to a navigation tree. A tree is accessed by your template by it's *"access name"*, and multiple trees can make use of the same *"menu item"* when necessary.

Trees are represented in django's ORM with the **NavigationTree** model. This model is fairly simple, and only contains the following properties:

* name - The human readable name for this specific **NavigationTree** instance.
* access_name - The name that will be supplied as a string to access this tree.

Leaves in the tree are represented by the **NavigationItem** model which describes a single link that can be assigned to a tree, and can also be assigned to a parent menu item for dropdowns.
