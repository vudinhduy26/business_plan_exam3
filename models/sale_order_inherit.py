from odoo import models, fields
from odoo.exceptions import MissingError, AccessError


class PlanSale(models.Model):
    _inherit = 'sale.order'
    business_plan = fields.Many2one(comodel_name='plan.sale.order')
    plan_state = fields.Selection(related='business_plan.state', string="Plan State")

    def action_create_plan(self):
        course_form = self.env['plan.sale.order']
        sale_order_id = self.id
        return {
            'name': 'New Course',
            'type': 'ir.actions.act_window',
            'res_model': 'plan.sale.order',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'views': [(course_form.id, 'form')],
            'view_id': 'course_form.id',
            'context': {'default_sale_order_id': sale_order_id},

        }

    def action_check_plan(self):
        for rec in self:
            if not rec.business_plan:
                raise MissingError("Plan doesn't exits")
            if rec.plan_state != 'accept':
                raise AccessError("Plan is not approval")
            else:
                message_id = self.env['message.wizard'].create({'message': "Plan approval"})
                return {
                    'name': 'Successfull',
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form',
                    'res_model': 'message.wizard',
                    'res_id': message_id.id,
                    'target': 'new'
                }

    # action click button  "Confirm the order."
    def confirm_order(self):
        for record in self:
            record.state = 'done'

    # action show view plan
    def action_view_plan(self):
        action = self.env["ir.actions.actions"]._for_xml_id("business_plan_managers_copy.action_product_warranty")
        plan_ids = self.business_plan.ids
        if len(plan_ids) == 1:
            res = self.env.ref('business_plan_managers_copy.view_plan_sale_order_form')
            form_view = [(res and res.id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state, view) for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = plan_ids[0]
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action
