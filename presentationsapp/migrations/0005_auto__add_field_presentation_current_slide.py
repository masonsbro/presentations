# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Presentation.current_slide'
        db.add_column(u'presentationsapp_presentation', 'current_slide',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='curpres', null=True, to=orm['presentationsapp.Slide']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Presentation.current_slide'
        db.delete_column(u'presentationsapp_presentation', 'current_slide_id')


    models = {
        u'presentationsapp.presentation': {
            'Meta': {'object_name': 'Presentation'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['presentationsapp.User']"}),
            'current_slide': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'curpres'", 'null': 'True', 'to': u"orm['presentationsapp.Slide']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'first_slide': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['presentationsapp.Slide']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'presentationsapp.slide': {
            'Meta': {'object_name': 'Slide'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'next': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['presentationsapp.Slide']", 'null': 'True'})
        },
        u'presentationsapp.user': {
            'Meta': {'object_name': 'User'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'password_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'reset_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['presentationsapp']