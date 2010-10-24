from django.db import models
from django.template.defaultfilters import slugify

USER_VISIBILITY_CHOICES = (
    (0, 'Everyone'),
    (1, 'Registered Users'),
    (2, 'Staff'),
    (3, 'Superusers'),
)

class NavigationTree(models.Model):
    name = models.CharField(max_length=16)
    access_name = models.CharField(max_length=16, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_trunk(self):
        return NavigationItem.objects.filter(tree=self, parent=None).all().order_by('priority')

    def save(self):
        if self.access_name == "":
            self.access_name = slugify(self.name).replace('-', '_')

        super(NavigationTree, self).save()

class NavigationItem(models.Model):
    label = models.CharField(max_length=32)
    title = models.CharField(max_length=128, blank=True, null=True)
    location = models.CharField(max_length=256)
    priority = models.PositiveIntegerField(default=0)

    parent = models.ForeignKey('self', blank=True, null=True,
        related_name='children')

    tree = models.ForeignKey(NavigationTree, blank=True, null=True,
                                  help_text="A navigation tree is a certain collection of"
                                      "navigation items, so that different navigation bars"
                                      "can exist.")

    user_visibility = models.PositiveIntegerField(max_length=1,
                                                  choices=USER_VISIBILITY_CHOICES,
                                                  default=USER_VISIBILITY_CHOICES[0][0])

    def zombie(self):
        return ((self.parent == None) and (self.tree == None))

    def get_children(self):
        return self.children.all().order_by('priority')

    def __unicode__(self):
        return self.label

