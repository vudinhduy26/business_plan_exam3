from datetime import datetime

from odoo import models, api, fields
from odoo.exceptions import ValidationError


class PlanSaleOrder(models.Model):
    _name = "plan.sale.order"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Text(string="Name")
    sale_order_id = fields.Many2one(comodel_name='sale.order', readonly=1)
    business_information = fields.Text(string='Business Information', required=True)
    state = fields.Selection([('new', 'New'), ('sent', 'Plan Sent'), ('accept', 'Accept'), ('cancel', 'Cancel')],
                             string='Action Plan', default='new')
    approver_lines = fields.One2many('approval.line', 'plan_id', string='Approver Lines')
    sale_order_state = fields.Selection(related='sale_order_id.state', string="Order State")

    def send_mail_template(self):
        #ids = self.env.context['active_ids']
        for record in self:
            record.state = 'sent'
            record.sale_order_id.business_plan = record.id
            partner_ids = []
            for line in record.approver_lines:
                partner_ids.append(line.user_id.partner_id.id)
            body = "A business plan has been created that needs approval! " + datetime.now().strftime(
                "%H:%M:%S  %d/%m/%Y")
            record.sale_order_id.message_post(message_type='notification', partner_ids=partner_ids, body=body)

        message_id = self.env['message.wizard'].sudo().create({'message': "Invitation is successfully sent"})
        return {
            'name': 'Successfully',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'message.wizard',
            'res_id': message_id.id,
            'target': 'new'
        }
