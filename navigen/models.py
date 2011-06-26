from django.db import models
from django.contrib.auth.models import Permission
from django.template.defaultfilters import slugify

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
    required_permissions = models.ManyToManyField(Permission, null=True, blank=True)
    staff_only = models.BooleanField(default=False)
    guests_only = models.BooleanField(default=False)
    guests_hidden = models.BooleanField(default=False)

    parent = models.ForeignKey('self', blank=True, null=True,
        related_name='children')

    tree = models.ManyToManyField(NavigationTree, blank=True, null=True,
                                  help_text="A navigation tree is a certain collection of"
                                      "navigation items, so that different navigation bars"
                                      "can exist.")

    def get_children(self):
        return self.children.all().order_by('priority')

    def __unicode__(self):
        return self.label

