def _item_is_active(request, item):
    return (item.location == request.GET('REQUEST_URI'))

def navigation_items(request):
    from models import NavigationItem, NavigationTree

    navigation_trees = NavigationTree.objects.all()
    navigation_items = {}

    for tree in navigation_trees:
        navigation_items['navigation_%s' % tree.access_name] = NavigationItem.objects.filter(tree=tree, parent=None).order_by('priority')

    return navigation_items
