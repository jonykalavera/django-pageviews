# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'HitCount.created'
        db.delete_column(u'pageviews_hitcount', 'created')

        # Deleting field 'HitCount.modified'
        db.delete_column(u'pageviews_hitcount', 'modified')

        # Adding field 'HitCount.created_at'
        db.add_column('pageviews_hitcount', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 3, 3, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'HitCount.updated_at'
        db.add_column('pageviews_hitcount', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 3, 3, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'HitCount.content_type'
        db.add_column('pageviews_hitcount', 'content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True),
                      keep_default=False)

        # Adding field 'HitCount.object_id'
        db.add_column('pageviews_hitcount', 'object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Adding field 'HitCount.for_date'
        db.add_column('pageviews_hitcount', 'for_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 3, 3, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'HitCount.created'
        db.add_column(u'pageviews_hitcount', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 3, 3, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'HitCount.modified'
        db.add_column(u'pageviews_hitcount', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 3, 3, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'HitCount.created_at'
        db.delete_column('pageviews_hitcount', 'created_at')

        # Deleting field 'HitCount.updated_at'
        db.delete_column('pageviews_hitcount', 'updated_at')

        # Deleting field 'HitCount.content_type'
        db.delete_column('pageviews_hitcount', 'content_type_id')

        # Deleting field 'HitCount.object_id'
        db.delete_column('pageviews_hitcount', 'object_id')

        # Deleting field 'HitCount.for_date'
        db.delete_column('pageviews_hitcount', 'for_date')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pageviews.hitcount': {
            'Meta': {'ordering': "('-created_at', '-updated_at')", 'object_name': 'HitCount'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'for_date': ('django.db.models.fields.DateTimeField', [], {}),
            'hits': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        }
    }

    complete_apps = ['pageviews']