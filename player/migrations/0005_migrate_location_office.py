
from south.db import db
from django.db import models
from labgeeksrpg.player.models import *

class Migration:

    no_dry_run = True
    
    def forwards(self, orm):
        for player in orm.Player.objects.all():
            player.office = player.location
    
    
    def backwards(self, orm):
        for player in orm.Player.objects.all():
            player.location = player.office
    
    
    models = {
        'player.player': {
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'aim_iChat': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'alt_phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'currency': ('django.db.models.fields.IntegerField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gmail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'grad_date': ('django.db.models.fields.DateField', [], {}),
            'hp': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'irc_network': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'irc_nick': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'middlename': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'uw_gmail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'uw_windows_live': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'uwnetid': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'windows_live': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'xp': ('django.db.models.fields.IntegerField', [], {}),
            'yahoo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'})
        },
        'player.playerreview': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'player.playerwagehistory': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'player.position': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'player.skills': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['player']