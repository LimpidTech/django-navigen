from django import template
from django.template.loader import get_template
from django.conf import settings
from navigation.models import NavigationTree, NavigationItem

register = template.Library()

class NavigationTreeNode(template.Node):
    tree_name = None

    def __init__(self, tree_name):
        self.tree_name = template.Variable(tree_name)

    def get_leaves(self, leaves, final_output=''):
        t = get_template('navigation/nav_list.html')

        c = template.Context({
            'leaves': leaves,
            'hey': 'okay',
        })

        return t.render(c)

    def get_tree(self, tree):
        t = get_template('navigation/tree.html')
        c = template.Context(
            {
                'branch': tree.get_trunk()
            }
        )

        return t.render(c)

    def render(self, context):
        try:
            tree = NavigationTree.objects.get(access_name=self.tree_name.resolve(context))

            return self.get_tree(tree)

        except template.VariableDoesNotExist:
            return ''

@register.tag(name='navtree')
def navtree(parser, token):
    try:
        tag_name, tree_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires exactly 1 argument"

    return NavigationTreeNode(tree_name)

class NavigationBranchNode(template.Node):
    branch = None

    def __init__(self, branch):
        self.branch = template.Variable(branch)

    def render(self, context):
        try:
            t = get_template('navigation/branch.html')
            c = template.Context(
                {
                    'branch': self.branch.resolve(context)
                }
            )

        except template.VariableDoesNotExist:
            return ''

        return t.render(c)

@register.tag(name='navbranch')
def navbranch(parser, token):
    try:
        tag_name, branch = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires exactly 1 argument"

    return NavigationBranchNode(branch)
