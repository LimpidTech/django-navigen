from django import template
from django.template.loader import get_template
from django.conf import settings
from navigation.models import NavigationTree, NavigationItem

register = template.Library()

class NavigationTreeNode(template.Node):
    tree_name = None
    user = None

    def __init__(self, tree_name, user):
        self.tree_name = template.Variable(tree_name)
        self.user = template.Variable(user)

    def get_leaves(self, leaves, final_output=''):
        t = get_template('navigation/nav_list.html')

        c = template.Context({
            'leaves': leaves,
            'hey': 'okay',
        })

        return t.render(c)

    def get_tree(self, tree, user):
        t = get_template('navigation/tree.html')
        c = template.Context(
            {
                'branch': tree.get_trunk(),
                'user': user 
            }
        )

        return t.render(c)

    def render(self, context):
        try:
            tree = NavigationTree.objects.get(access_name=self.tree_name.resolve(context))

            return self.get_tree(tree, self.user.resolve(context))

        except template.VariableDoesNotExist:
            return ''

@register.tag(name='navtree')
def navtree(parser, token):
    try:
        tag_name, tree_name, user = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires exactly 1 argument"

    return NavigationTreeNode(tree_name, user)

class NavigationBranchNode(template.Node):
    branch = None
    user = None

    def __init__(self, branch, user):
        self.branch = template.Variable(branch)
        self.user = template.Variable(user)

    def render(self, context):
        try:
            t = get_template('navigation/branch.html')
            c = template.Context(
                {
                    'branch': self.branch.resolve(context),
                    'user': self.user.resolve(context),
                    'list_a': [1,2,3,4],
                    'list_b': [1,2,3,4,5,6,7,8,9],
                }
            )

        except template.VariableDoesNotExist:
            return ''

        return t.render(c)

@register.tag(name='navbranch')
def navbranch(parser, token):
    try:
        tag_name, branch, user = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires exactly 1 argument"

    return NavigationBranchNode(branch, user)


@register.filter(name='list_items_in_list')
def list_items_in_list(needles, haystack):
    for value in haystack:
        if value not in needles:
            return False

    return True

