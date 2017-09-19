# -*- coding: utf-8 -*-
from odoo import http

# class Odoo-custom-module-example2(http.Controller):
#     @http.route('/odoo-custom-module-example2/odoo-custom-module-example2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-custom-module-example2/odoo-custom-module-example2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-custom-module-example2.listing', {
#             'root': '/odoo-custom-module-example2/odoo-custom-module-example2',
#             'objects': http.request.env['odoo-custom-module-example2.odoo-custom-module-example2'].search([]),
#         })

#     @http.route('/odoo-custom-module-example2/odoo-custom-module-example2/objects/<model("odoo-custom-module-example2.odoo-custom-module-example2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-custom-module-example2.object', {
#             'object': obj
#         })