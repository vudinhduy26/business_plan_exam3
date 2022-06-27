# -*- coding: utf-8 -*-
# from odoo import http


# class BusinessPlanManagersCopy(http.Controller):
#     @http.route('/business_plan_managers_copy/business_plan_managers_copy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/business_plan_managers_copy/business_plan_managers_copy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('business_plan_managers_copy.listing', {
#             'root': '/business_plan_managers_copy/business_plan_managers_copy',
#             'objects': http.request.env['business_plan_managers_copy.business_plan_managers_copy'].search([]),
#         })

#     @http.route('/business_plan_managers_copy/business_plan_managers_copy/objects/<model("business_plan_managers_copy.business_plan_managers_copy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('business_plan_managers_copy.object', {
#             'object': obj
#         })
