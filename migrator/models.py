from django.db import models

class IMAPEndpoint(models.Model):
    """ An imap account definition
    """
    login = models.EmailField(verbose_name='email')
    password = models.CharField(max_length=200)
    host = models.CharField(max_length=100)
    port = models.IntegerField(default=143)
    encryption = models.CharField(max_length=100)
    dossier_racine = models.CharField(max_length=200)

    def __str__(self):
        #return "host : %s" % self.host
        return "{} on {}".format(self.login, self.host)


class Migration(models.Model):
    source = models.OneToOneField(IMAPEndpoint, related_name='target_migration')
    target = models.OneToOneField(IMAPEndpoint, related_name='source_migration')
    creation_date = models.DateTimeField('Date créée')
    processing_date = models.DateTimeField('Date de démarrage')
    completion_date = models.DateTimeField('Date de fin')

    def __str__(self):
        return "Source : %s" % self.source