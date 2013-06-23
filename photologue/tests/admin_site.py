#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.test import RequestFactory
from photologue.admin import PhotoAdmin
from photologue.models import Photo
from photologue.tests.helpers import PhotologueBaseTest


class PhotoAdminTest(PhotologueBaseTest):
    def test_should_render_custom_template_on_changelist(self):
        admin_site = AdminSite('Test Admin')
        photo_admin = PhotoAdmin(Photo, admin_site)
        user = User.objects.create_superuser('test1', 'test@example.com',
                                              'pass')

        factory = RequestFactory()
        request = factory.get('/admin/photologue/photo/')
        request.user = user
        response = photo_admin.changelist_view(request)

        self.assertIn('admin/photologue/photo/change_list.html', response.template_name)
